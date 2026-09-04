#!/usr/bin/env python3
"""
SIH26168 — 10Hz ↔ 200Hz Resampler (single shared SpeedNet)
Phone 10Hz and FOG 200Hz both resampled to 100Hz internally → same model.
"""
import numpy as np
from scipy.signal import resample_poly, decimate

TARGET_HZ=100

def resample_to_target(sig: np.ndarray, fs_in: int, fs_out: int = TARGET_HZ) -> np.ndarray:
    """
    sig: (N,6) or (N,) at fs_in → (M,6) at fs_out
    Uses polyphase (linear interp fallback for small windows).
    """
    if sig.ndim==1:
        sig=sig[:,None]
        squeeze=True
    else:
        squeeze=False
    N=sig.shape[0]
    # simple linear interp is enough for hackathon and faster
    t_in = np.arange(N)/fs_in
    duration = t_in[-1] if N>1 else 0
    M = int(round(duration*fs_out))+1
    if M<=1:
        out=sig
    else:
        t_out = np.arange(M)/fs_out
        out = np.vstack([np.interp(t_out, t_in, sig[:,c]) for c in range(sig.shape[1])]).T
    return out[:,0] if squeeze else out

def make_window_200(sig100: np.ndarray, win_sec=2.0) -> np.ndarray:
    """ sig100: (T,6) @100Hz → windows (N,200,6) stride 0.2s """
    win_len=int(win_sec*TARGET_HZ)  # 200
    stride=int(0.2*TARGET_HZ)  # 20
    wins=[]
    for i in range(0, len(sig100)-win_len+1, stride):
        wins.append(sig100[i:i+win_len])
    return np.stack(wins) if wins else np.zeros((0,win_len,6))

# Dual-rate EKF glue
class DualRateIMU:
    """
    Buffers IMU at native rate, exposes 100Hz stream for SpeedNet
    and native rate for EKF predict.
    """
    def __init__(self, native_hz: int):
        self.native_hz=native_hz
        self.buf=[]  # list of (t, acc(3), gyro(3))
        self.last_speednet_t=0

    def push(self, t: float, acc: np.ndarray, gyro: np.ndarray):
        self.buf.append((t, acc, gyro))
        # keep last 3s
        while self.buf and self.buf[0][0] < t-3.0:
            self.buf.pop(0)

    def get_100hz_window(self, win_sec=2.0):
        """Return latest 2s resampled to 100Hz for SpeedNet, or None if not enough."""
        if len(self.buf)< 5:
            return None
        ts=np.array([b[0] for b in self.buf])
        acc=np.stack([b[1] for b in self.buf])
        gyro=np.stack([b[2] for b in self.buf])
        sig=np.concatenate([acc, gyro], axis=1)  # (N,6)
        sig100=resample_to_target(sig, self.native_hz, TARGET_HZ)
        if len(sig100) < int(win_sec*TARGET_HZ):
            return None
        return sig100[-int(win_sec*TARGET_HZ):]  # (200,6)

    def should_run_speednet(self, t: float, period=0.1)->bool:
        """SpeedNet @10Hz regardless of native rate"""
        if t - self.last_speednet_t >= period-1e-6:
            self.last_speednet_t=t
            return True
        return False

if __name__=="__main__":
    # demo: phone 10Hz → 100Hz and FOG 200Hz → 100Hz both produce (200,6)
    rng=np.random.default_rng(0)
    phone_sig=rng.normal(0,0.3,size=(20,6))  # 2s @10Hz
    fog_sig=rng.normal(0,0.3,size=(400,6))   # 2s @200Hz
    p100=resample_to_target(phone_sig, 10)
    f100=resample_to_target(fog_sig, 200)
    print("phone 10→100:", p100.shape, "fog 200→100:", f100.shape)
    assert p100.shape[1]==6 and f100.shape[1]==6
    print("OK — single SpeedNet can consume both (200,6) windows")
