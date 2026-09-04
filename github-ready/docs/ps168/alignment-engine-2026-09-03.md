# SIH26168 — Alignment Engine (Phone→Vehicle Rotation)
**Date:** 2026-09-03 | **Researcher:** @researcher | **Iteration:** 1/4
**Status:** COMPLETE — Mathematical derivation + Python implementation + validation plan

---

## Problem: Phone Mount Misalignment

**Reality:** Phone in holder ≠ vehicle frame
- Phone yaw offset: ±15° typical (holder slack)
- Phone pitch/roll: ±10° (dashboard angle)
- Phone slides during driving → time-varying misalignment
- **Without alignment:** Lateral velocity leaks into forward → 5× drift

**PS Requirement:** "Online mount-aided attitude estimation" — auto-calibrate in <15s, re-estimate every 30s.

---

## Mathematical Derivation

### Coordinate Frames
- **V (Vehicle):** x=forward, y=left, z=up (ENU)
- **P (Phone):** x=right, y=up, z=out-of-screen (Android sensor frame)

### Goal: Find R_P→V (3×3 rotation matrix)

### Method: PCA on Acceleration During Straight Driving

**Assumption:** During straight-line driving with good GNSS:
- Vehicle acceleration ≈ [a_x, 0, -g] in V-frame (forward accel, gravity)
- Phone measures same acceleration in P-frame: a_P = R_V→P · a_V
- The **forward direction in phone frame** = principal component of acceleration

### Algorithm

```python
import numpy as np
from scipy.linalg import eigh

def estimate_alignment(acc_phone: np.ndarray, gnss_speed: np.ndarray, 
                       gnss_heading: np.ndarray, dt: float = 0.1) -> np.ndarray:
    """
    Estimate R_phone_to_vehicle from IMU + GNSS during straight driving.
    
    Args:
        acc_phone: (N, 3) accelerometer in phone frame [m/s²]
        gnss_speed: (N,) speed from GNSS [m/s]
        gnss_heading: (N,) heading from GNSS [rad]
        dt: sample period [s] (0.1 for 10Hz)
    
    Returns:
        R_p2v: (3, 3) rotation matrix from phone to vehicle frame
    """
    
    # 1. Detect straight driving segments
    # Low lateral acceleration + steady heading + good GNSS
    speed_diff = np.abs(np.gradient(gnss_speed, dt))
    heading_rate = np.abs(np.gradient(gnss_heading, dt))
    
    straight_mask = (
        (speed_diff < 0.5) &           # Not accelerating hard
        (heading_rate < 0.05) &        # Not turning (≈3°/s)
        (gnss_speed > 5.0)             # Moving fast enough (>18 km/h)
    )
    
    if straight_mask.sum() < 30:  # Need at least 3s @ 10Hz
        return None  # Insufficient data
    
    # 2. Extract straight segments
    acc_straight = acc_phone[straight_mask]  # (M, 3)
    
    # 3. Remove gravity (estimate from low-pass filtered acc)
    # Gravity ≈ mean acceleration when stationary, but we use straight driving
    # High-pass filter to get dynamic acceleration
    from scipy.signal import butter, filtfilt
    b, a = butter(2, 0.5 / (0.5 / dt), btype='highpass')  # 0.5 Hz cutoff
    acc_dynamic = filtfilt(b, a, acc_straight, axis=0)
    
    # 4. PCA on dynamic acceleration covariance
    cov = acc_dynamic.T @ acc_dynamic / len(acc_dynamic)  # (3, 3)
    eigvals, eigvecs = eigh(cov)  # Ascending order
    
    # Principal component = eigenvector with largest eigenvalue
    # This is the PRIMARY ACCELERATION DIRECTION in phone frame
    forward_phone = eigvecs[:, -1]  # Last column = largest eigenvalue
    
    # Ensure forward_phone points forward (positive correlation with speed increase)
    if np.corrcoef(acc_dynamic @ forward_phone, speed_diff[straight_mask])[0, 1] < 0:
        forward_phone = -forward_phone
    
    # 5. Gravity vector in phone frame (from static periods or low-pass)
    # Use low-pass filtered acceleration during straight driving
    b_lp, a_lp = butter(2, 0.1 / (0.5 / dt), btype='lowpass')  # 0.1 Hz
    acc_static = filtfilt(b_lp, a_lp, acc_straight, axis=0)
    gravity_phone = -np.mean(acc_static, axis=0)  # Negative because acc measures -g
    gravity_phone = gravity_phone / np.linalg.norm(gravity_phone)
    
    # 6. Construct vehicle frame axes in phone coordinates
    # Vehicle x (forward) = forward_phone
    # Vehicle z (up) = gravity_phone (opposite of gravity)
    # Vehicle y (left) = z × x (right-hand rule)
    
    x_v_in_p = forward_phone
    z_v_in_p = gravity_phone
    y_v_in_p = np.cross(z_v_in_p, x_v_in_p)
    y_v_in_p = y_v_in_p / np.linalg.norm(y_v_in_p)
    
    # Re-orthogonalize x (in case gravity not perfectly perpendicular)
    x_v_in_p = np.cross(y_v_in_p, z_v_in_p)
    x_v_in_p = x_v_in_p / np.linalg.norm(x_v_in_p)
    
    # 7. R_phone_to_vehicle: columns are vehicle axes expressed in phone frame
    # Actually we want R such that v_V = R_P→V @ v_P
    # So rows of R_P→V are vehicle axes in phone frame
    R_p2v = np.vstack([x_v_in_p, y_v_in_p, z_v_in_p])  # (3, 3)
    
    # Verify: R_p2v @ gravity_phone ≈ [0, 0, -1] (gravity in vehicle frame)
    # Verify: R_p2v @ forward_phone ≈ [1, 0, 0] (forward in vehicle frame)
    
    return R_p2v
```

### Alternative: GNSS Heading + Acceleration Fusion

When GNSS heading is reliable (HDOP < 2, sats > 8):

```python
def estimate_alignment_gnss(acc_phone: np.ndarray, gnss_heading: np.ndarray,
                            gnss_speed: np.ndarray, dt: float = 0.1) -> np.ndarray:
    """
    Use GNSS heading to directly solve for yaw, then pitch/roll from gravity.
    """
    straight_mask = (np.abs(np.gradient(gnss_speed, dt)) < 0.5) & (gnss_speed > 5.0)
    
    if straight_mask.sum() < 20:
        return None
    
    # Mean heading during straight segment = vehicle yaw
    yaw_v = np.median(gnss_heading[straight_mask])
    
    # Gravity in phone frame (low-pass acc)
    from scipy.signal import butter, filtfilt
    b, a = butter(2, 0.1 / (0.5 / dt), btype='lowpass')
    acc_static = filtfilt(b, a, acc_phone[straight_mask], axis=0)
    gravity_p = -np.mean(acc_static, axis=0)
    gravity_p = gravity_p / np.linalg.norm(gravity_p)
    
    # Vehicle frame: x=forward(cos yaw, sin yaw), y=left(-sin yaw, cos yaw), z=up
    # But we need phone→vehicle rotation
    # Phone measures gravity_p = R_V→P @ [0, 0, -1]
    # So R_V→P @ [0, 0, -1] = gravity_p
    
    # Decompose gravity_p into pitch/roll
    pitch = np.arcsin(np.clip(gravity_p[0], -1, 1))  # x-axis tilt
    roll = np.arctan2(-gravity_p[1], -gravity_p[2])   # y/z tilt
    
    # R_P→V = R_z(yaw) @ R_y(pitch) @ R_x(roll)  (but inverted)
    # Actually: v_V = R_z(-yaw) @ R_y(-pitch) @ R_x(-roll) @ v_P
    
    cy, sy = np.cos(-yaw_v), np.sin(-yaw_v)
    cp, sp = np.cos(-pitch), np.sin(-pitch)
    cr, sr = np.cos(-roll), np.sin(-roll)
    
    Rz = np.array([[cy, -sy, 0], [sy, cy, 0], [0, 0, 1]])
    Ry = np.array([[cp, 0, sp], [0, 1, 0], [-sp, 0, cp]])
    Rx = np.array([[1, 0, 0], [0, cr, -sr], [0, sr, cr]])
    
    R_p2v = Rz @ Ry @ Rx
    
    return R_p2v
```

---

## Online Calibration UI

```python
class AlignmentEngine:
    def __init__(self):
        self.R_p2v = None
        self.calibration_state = "WAITING"  # WAITING, CALIBRATING, ALIGNED, REFINING
        self.calibration_buffer = {"acc": [], "gnss_speed": [], "gnss_heading": []}
        self.calibration_start_time = None
        self.last_refine_time = 0
    
    def update(self, acc: np.ndarray, gnss_speed: float, gnss_heading: float, 
               gnss_hdop: float, gnss_sats: int, timestamp: float):
        """Call at 10Hz with new sensor data"""
        
        # Only calibrate with good GNSS
        gnss_good = (gnss_hdop < 2.0) and (gnss_sats >= 8) and (gnss_speed > 3.0)
        
        if self.calibration_state == "WAITING":
            if gnss_good:
                self.calibration_state = "CALIBRATING"
                self.calibration_start_time = timestamp
                self.calibration_buffer = {"acc": [], "gnss_speed": [], "gnss_heading": []}
        
        elif self.calibration_state == "CALIBRATING":
            if gnss_good:
                self.calibration_buffer["acc"].append(acc)
                self.calibration_buffer["gnss_speed"].append(gnss_speed)
                self.calibration_buffer["gnss_heading"].append(gnss_heading)
            
            elapsed = timestamp - self.calibration_start_time
            remaining = max(0, 15 - elapsed)
            
            if elapsed >= 15 or len(self.calibration_buffer["acc"]) >= 150:
                # Attempt calibration
                acc_arr = np.array(self.calibration_buffer["acc"])
                speed_arr = np.array(self.calibration_buffer["gnss_speed"])
                heading_arr = np.array(self.calibration_buffer["gnss_heading"])
                
                # Try PCA method first
                R = estimate_alignment(acc_arr, speed_arr, heading_arr)
                
                if R is not None:
                    self.R_p2v = R
                    self.calibration_state = "ALIGNED"
                    self.last_refine_time = timestamp
                    return {"state": "ALIGNED", "R": R, "message": "Aligned ✓"}
                else:
                    # Reset and retry
                    self.calibration_state = "WAITING"
                    return {"state": "WAITING", "message": "Need more straight driving"}
            
            return {"state": "CALIBRATING", "remaining_sec": int(remaining)}
        
        elif self.calibration_state == "ALIGNED":
            # Periodic refinement every 30s during driving
            if gnss_good and (timestamp - self.last_refine_time) > 30:
                self.calibration_state = "REFINING"
                self.calibration_buffer = {"acc": [], "gnss_speed": [], "gnss_heading": []}
                self.calibration_start_time = timestamp
            
            return {"state": "ALIGNED", "R": self.R_p2v}
        
        elif self.calibration_state == "REFINING":
            if gnss_good:
                self.calibration_buffer["acc"].append(acc)
                self.calibration_buffer["gnss_speed"].append(gnss_speed)
                self.calibration_buffer["gnss_heading"].append(gnss_heading)
            
            elapsed = timestamp - self.calibration_start_time
            
            if elapsed >= 10 or len(self.calibration_buffer["acc"]) >= 100:
                acc_arr = np.array(self.calibration_buffer["acc"])
                speed_arr = np.array(self.calibration_buffer["gnss_speed"])
                heading_arr = np.array(self.calibration_buffer["gnss_heading"])
                
                R_new = estimate_alignment(acc_arr, speed_arr, heading_arr)
                
                if R_new is not None:
                    # Smooth update (exponential moving average on rotation manifold)
                    self.R_p2v = self._slerp_rotation(self.R_p2v, R_new, alpha=0.3)
                    self.last_refine_time = timestamp
                
                self.calibration_state = "ALIGNED"
            
            return {"state": "ALIGNED", "R": self.R_p2v}
    
    def _slerp_rotation(self, R1, R2, alpha):
        """Spherical linear interpolation between rotation matrices"""
        # Convert to quaternions, slerp, convert back
        from scipy.spatial.transform import Rotation as R
        q1 = R.from_matrix(R1).as_quat()
        q2 = R.from_matrix(R2).as_quat()
        # Ensure shortest path
        if np.dot(q1, q2) < 0:
            q2 = -q2
        q_interp = q1 + alpha * (q2 - q1)
        q_interp = q_interp / np.linalg.norm(q_interp)
        return R.from_quat(q_interp).as_matrix()
    
    def get_ui_status(self):
        """Return status for UI display"""
        if self.calibration_state == "WAITING":
            return "🔄 Drive straight at >20 km/h with good GPS to calibrate"
        elif self.calibration_state == "CALIBRATING":
            elapsed = time.time() - self.calibration_start_time
            return f"📐 Calibrating... {max(0, 15-int(elapsed))}s remaining — keep driving straight"
        elif self.calibration_state == "REFINING":
            return "🔧 Refining alignment..."
        else:
            return "✅ Aligned — phone frame locked to vehicle"
```

---

## Validation on IO-VNBD

```python
def validate_alignment_on_iovnbd():
    """Test alignment engine on IO-VNBD smartphone data with ground truth"""
    # IO-VNBD has both phone IMU AND vehicle CAN (ground truth vehicle frame)
    # For synchronized sequences, we know the TRUE phone→vehicle rotation
    
    # Load synchronized S- and V- data for same route
    # V- data gives us vehicle-frame acceleration (from CAN)
    # S- data gives us phone-frame acceleration
    # True R = solve for rotation that aligns S-acc to V-acc
    
    # Metrics:
    # - Yaw error (degrees)
    # - Pitch/Roll error (degrees) 
    # - Forward speed correlation after alignment
    # - Time to calibrate (<15s target)
    
    pass  # Implementation in notebook
```

---

## Integration with EKF

```python
# In EKF predict step:
# 1. Raw phone IMU: acc_P, gyro_P
# 2. Transform to vehicle frame:
acc_V = R_p2v @ acc_P
gyro_V = R_p2v @ gyro_P
# 3. Use acc_V, gyro_V in EKF (standard vehicle-frame INS)
# 4. NHC: v_y ≈ 0, v_z ≈ 0 in VEHICLE frame (now correct!)
```

---

## Key Parameters for Hackathon

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Calibration duration | 15s | PS requirement: <15s |
| Min speed for calibration | 5 m/s (18 km/h) | Sufficient dynamic accel |
| Max heading rate | 0.05 rad/s (3°/s) | Straight driving |
| Refinement interval | 30s | Handle phone slip |
| Smoothing alpha | 0.3 | Stable but adaptive |
| GNSS HDOP threshold | < 2.0 | Reliable heading |
| GNSS sats threshold | ≥ 8 | Good geometry |

---

## Sources Cited

1. IO-VNBD Paper: https://arxiv.org/abs/2005.01701 — Phone vs vehicle sensor specs
2. AVNet (Qian et al., 2025) — Invariant EKF with online alignment
3. RoNIN (Yan et al., IROS 2019) — Phone IMU orientation estimation
4. PDR literature — ZUPT, NHC, alignment methods
5. filterpy / eskf Python libraries — EKF implementation reference