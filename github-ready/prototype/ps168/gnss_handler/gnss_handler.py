#!/usr/bin/env python3
"""
SIH26168 — Seamless GNSS Deficit Handler
- Detects outage in <200ms (3 samples @10Hz)
- Freezes GNSS gain, inflates Q, runs INS+NHC+Map
- On recovery: weighted re-seed without position jump
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class GnssSample:
    hdop: float
    sats: int
    vel_conf: float  # 0..1
    pos: tuple  # (x,y,z) or None
    vel: tuple  # (vx,vy,vz) or None

class GnssHandler:
    def __init__(self, hdop_thr=3.0, sats_thr=4, conf_thr=0.5, outage_confirm=3, recovery_confirm=5):
        self.hdop_thr=hdop_thr
        self.sats_thr=sats_thr
        self.conf_thr=conf_thr
        self.outage_confirm=outage_confirm
        self.recovery_confirm=recovery_confirm
        self.state="GNSS_OK"  # GNSS_OK | OUTAGE
        self.outage_counter=0
        self.recovery_counter=0
        self.outage_duration=0.0
        self.outage_start_t=None

    def _is_bad(self, s: GnssSample)->bool:
        return (s.hdop > self.hdop_thr) or (s.sats < self.sats_thr) or (s.vel_conf < self.conf_thr) or (s.pos is None)

    def update(self, sample: GnssSample, t: float, ekf) -> dict:
        """
        Call at 10 Hz. Returns dict with action for EKF.
        ekf is expected to have .P (cov), .x, and methods .set_gnss_gain(), .inflate_Q(), .update_gnss()
        """
        bad = self._is_bad(sample)
        info={"state":self.state, "bad":bad, "action":"none"}

        if self.state=="GNSS_OK":
            if bad:
                self.outage_counter+=1
                if self.outage_counter >= self.outage_confirm:  # <200ms @10Hz with 3
                    self.state="OUTAGE"
                    self.outage_start_t=t
                    self.outage_duration=0
                    self.recovery_counter=0
                    # Freeze GNSS correction
                    if hasattr(ekf, "set_gnss_gain"): ekf.set_gnss_gain(0.0)
                    if hasattr(ekf, "inflate_Q"): ekf.inflate_Q(factor=2.0)
                    info["action"]="enter_outage"
            else:
                self.outage_counter=0
                # Normal GNSS update
                if sample.pos is not None and hasattr(ekf, "update_gnss"):
                    # adaptive R by HDOP
                    R_scale = 1.0 + 2.0*max(0, sample.hdop-1)
                    ekf.update_gnss(sample.pos, sample.vel, R_scale=R_scale)
                    info["action"]="gnss_update"
            info["state"]=self.state
            return info

        else: # OUTAGE
            self.outage_duration = t - (self.outage_start_t or t)
            if not bad:
                self.recovery_counter+=1
                if self.recovery_counter >= self.recovery_confirm:
                    # Recovery: decide hard vs soft
                    # innovation check
                    try:
                        import numpy as np
                        innov = np.array(sample.pos) - ekf.x[0:3]
                        # position covariance
                        P_pos = ekf.P[0:3,0:3] if hasattr(ekf.P, "shape") else None
                        if P_pos is not None:
                            dist = float(np.linalg.norm(innov))
                            sigma = float(np.sqrt(np.trace(P_pos)/3))
                            if dist > 3*max(sigma, 3.0):
                                # hard re-seed (large jump would look broken otherwise, but we smooth)
                                if hasattr(ekf, "reseed_position"):
                                    ekf.reseed_position(sample.pos, smooth_alpha=0.3)
                                info["action"]="hard_reseed"
                            else:
                                if hasattr(ekf, "update_gnss"):
                                    R_scale = 1.0 + 2.0*max(0, sample.hdop-1)
                                    ekf.update_gnss(sample.pos, sample.vel, R_scale=R_scale*0.5)
                                info["action"]="soft_fusion"
                        else:
                            if hasattr(ekf, "update_gnss"):
                                ekf.update_gnss(sample.pos, sample.vel, R_scale=1.0)
                            info["action"]="soft_fusion"
                    except Exception:
                        info["action"]="soft_fusion"
                    # restore
                    self.state="GNSS_OK"
                    self.outage_counter=0
                    self.recovery_counter=0
                    if hasattr(ekf, "set_gnss_gain"): ekf.set_gnss_gain(1.0)
                    if hasattr(ekf, "restore_Q"): ekf.restore_Q()
                    info["state"]=self.state
                    info["outage_duration"]=self.outage_duration
                    return info
                else:
                    info["action"]="recovery_pending"
            else:
                self.recovery_counter=0
                info["action"]="in_outage"
                # keep INS+NHC+Map only
            info["state"]=self.state
            info["outage_duration"]=self.outage_duration
            return info

    def badge(self)->str:
        if self.state=="OUTAGE":
            return f"GNSS→DR {int(self.outage_duration)}s"
        return "GNSS OK"

if __name__=="__main__":
    # smoke test
    class FakeEKF:
        def __init__(self):
            import numpy as np
            self.x=np.zeros(16)
            self.P=np.eye(15)*5
        def set_gnss_gain(self, g): pass
        def inflate_Q(self, factor): pass
        def restore_Q(self): pass
        def update_gnss(self, pos, vel, R_scale=1):
            import numpy as np
            self.x[0:3]=np.array(pos)
        def reseed_position(self, pos, smooth_alpha=0.3):
            import numpy as np
            self.x[0:3]= (1-smooth_alpha)*self.x[0:3]+smooth_alpha*np.array(pos)
    h=GnssHandler()
    ekf=FakeEKF()
    for t in range(100):
        # simulate: 20 good, 60 bad (tunnel), 20 good
        if 20 <= t < 80:
            s=GnssSample(hdop=99, sats=0, vel_conf=0, pos=None, vel=None)
        else:
            s=GnssSample(hdop=1.2, sats=8, vel_conf=0.9, pos=(t,0,0), vel=(5,0,0))
        print(t, h.update(s, t*0.1, ekf))
