import numpy as np
from numpy.linalg import inv, norm
from dataclasses import dataclass
from typing import Optional, Tuple

# ============================
# CONSTANTS
# ============================
G = np.array([0.0, 0.0, -9.80665])  # Gravity in vehicle frame (ENU: z down)
DEG2RAD = np.pi / 180.0

@dataclass
class EKFState:
    """16-state vector"""
    pos: np.ndarray      # (3,) - position [m] in ENU
    vel: np.ndarray      # (3,) - velocity [m/s] in ENU
    quat: np.ndarray     # (4,) - quaternion [w, x, y, z] vehicle->ENU
    acc_bias: np.ndarray # (3,) - accelerometer bias [m/s^2]
    gyro_bias: np.ndarray # (3,) - gyroscope bias [rad/s]
    
    def to_vector(self) -> np.ndarray:
        return np.concatenate([self.pos, self.vel, self.quat, self.acc_bias, self.gyro_bias])
    
    @classmethod
    def from_vector(cls, x: np.ndarray) -> 'EKFState':
        return cls(
            pos=x[0:3].copy(),
            vel=x[3:6].copy(),
            quat=x[6:10].copy(),
            acc_bias=x[10:13].copy(),
            gyro_bias=x[13:16].copy()
        )
    
    @property
    def dim(self) -> int:
        return 16

@dataclass
class EKFCovariance:
    """16x16 covariance matrix"""
    P: np.ndarray  # (16, 16)

@dataclass
class IMUData:
    acc: np.ndarray      # (3,) - accelerometer [m/s^2] in phone frame
    gyro: np.ndarray     # (3,) - gyroscope [rad/s] in phone frame
    dt: float            # time step [s]
    timestamp: float

@dataclass
class GNSSData:
    pos: np.ndarray      # (3,) - position [m] ENU
    vel: np.ndarray      # (3,) - velocity [m/s] ENU
    pos_cov: np.ndarray  # (3, 3)
    vel_cov: np.ndarray  # (3, 3)
    hdop: float
    sats: int
    timestamp: float

@dataclass
class AISpeedData:
    speed: float         # forward speed [m/s] from SpeedNet
    speed_std: float     # 1-sigma uncertainty
    timestamp: float

@dataclass
class MapMatchData:
    pos: np.ndarray      # (3,) - matched position [m] ENU
    pos_cov: np.ndarray  # (3, 3)
    timestamp: float


class DeadReckoningEKF:
    """
    Error-state EKF for INS/GNSS/AI/Map fusion
    """
    
    def __init__(self, R_phone_to_vehicle: np.ndarray):
        """
        R_phone_to_vehicle: (3, 3) rotation matrix from phone frame to vehicle frame
        Vehicle frame: x=forward, y=left, z=up
        """
        # State
        self.x = EKFState(
            pos=np.zeros(3),
            vel=np.zeros(3),
            quat=np.array([1.0, 0.0, 0.0, 0.0]),  # identity
            acc_bias=np.zeros(3),
            gyro_bias=np.zeros(3)
        )
        
        # Covariance
        self.P = np.diag([
            10.0, 10.0, 10.0,      # pos
            1.0, 1.0, 1.0,         # vel
            0.1, 0.1, 0.1, 0.1,    # quat
            0.01, 0.01, 0.01,      # acc bias
            0.001, 0.001, 0.001    # gyro bias
        ])
        
        # Phone-to-vehicle rotation (calibrated from alignment engine)
        self.R_p2v = R_phone_to_vehicle  # (3, 3)
        
        # Process noise (continuous-time spectral densities)
        self.q_acc = 0.01       # accel random walk [m/s^2/sqrt(Hz)]
        self.q_gyro = 0.0001    # gyro random walk [rad/s/sqrt(Hz)]
        self.q_acc_bias = 0.0001
        self.q_gyro_bias = 0.000001
        
        # NHC/ZUPT thresholds
        self.zupt_acc_thresh = 0.05   # m/s^2
        self.zupt_gyro_thresh = 0.005 # rad/s
        self.nhc_yaw_rate_thresh = 0.01  # rad/s
        
        # GNSS gating
        self.hdop_max = 3.0
        self.sats_min = 4
        self.innovation_gate = 3.0  # 3-sigma
        
        # Outage tracking
        self.gnss_outage = False
        self.outage_duration = 0.0
        
    # ============================
    # QUATERNION UTILITIES
    # ============================
    @staticmethod
    def quat_multiply(q1: np.ndarray, q2: np.ndarray) -> np.ndarray:
        """Hamilton product: q1 ⊗ q2"""
        w1, x1, y1, z1 = q1
        w2, x2, y2, z2 = q2
        return np.array([
            w1*w2 - x1*x2 - y1*y2 - z1*z2,
            w1*x2 + x1*w2 + y1*z2 - z1*y2,
            w1*y2 - x1*z2 + y1*w2 + z1*x2,
            w1*z2 + x1*y2 - y1*x2 + z1*w2
        ])
    
    @staticmethod
    def quat_conjugate(q: np.ndarray) -> np.ndarray:
        return np.array([q[0], -q[1], -q[2], -q[3]])
    
    @staticmethod
    def quat_rotate(q: np.ndarray, v: np.ndarray) -> np.ndarray:
        """Rotate vector v by quaternion q"""
        qv = np.array([0.0, v[0], v[1], v[2]])
        return DeadReckoningEKF.quat_multiply(
            DeadReckoningEKF.quat_multiply(q, qv),
            DeadReckoningEKF.quat_conjugate(q)
        )[1:]
    
    @staticmethod
    def quat_to_rotmat(q: np.ndarray) -> np.ndarray:
        """Quaternion to rotation matrix (vehicle->ENU)"""
        w, x, y, z = q
        return np.array([
            [1-2*(y*y+z*z), 2*(x*y-w*z), 2*(x*z+w*y)],
            [2*(x*y+w*z), 1-2*(x*x+z*z), 2*(y*z-w*x)],
            [2*(x*z-w*y), 2*(y*z+w*x), 1-2*(x*x+y*y)]
        ])
    
    @staticmethod
    def rotmat_to_quat(R: np.ndarray) -> np.ndarray:
        """Rotation matrix to quaternion"""
        tr = np.trace(R)
        if tr > 0:
            S = np.sqrt(tr + 1.0) * 2
            w = 0.25 * S
            x = (R[2,1] - R[1,2]) / S
            y = (R[0,2] - R[2,0]) / S
            z = (R[1,0] - R[0,1]) / S
        elif R[0,0] > R[1,1] and R[0,0] > R[2,2]:
            S = np.sqrt(1.0 + R[0,0] - R[1,1] - R[2,2]) * 2
            w = (R[2,1] - R[1,2]) / S
            x = 0.25 * S
            y = (R[0,1] + R[1,0]) / S
            z = (R[0,2] + R[2,0]) / S
        elif R[1,1] > R[2,2]:
            S = np.sqrt(1.0 + R[1,1] - R[0,0] - R[2,2]) * 2
            w = (R[0,2] - R[2,0]) / S
            x = (R[0,1] + R[1,0]) / S
            y = 0.25 * S
            z = (R[1,2] + R[2,1]) / S
        else:
            S = np.sqrt(1.0 + R[2,2] - R[0,0] - R[1,1]) * 2
            w = (R[1,0] - R[0,1]) / S
            x = (R[0,2] + R[2,0]) / S
            y = (R[1,2] + R[2,1]) / S
            z = 0.25 * S
        return np.array([w, x, y, z])
    
    # ============================
    # PREDICT (IMU @ 100Hz)
    # ============================
    def predict(self, imu: IMUData):
        """Time update with IMU measurement"""
        dt = imu.dt
        
        # Remove bias
        acc_corrected = imu.acc - self.x.acc_bias
        gyro_corrected = imu.gyro - self.x.gyro_bias
        
        # Rotate to vehicle frame
        acc_v = self.R_p2v @ acc_corrected
        gyro_v = self.R_p2v @ gyro_corrected
        
        # Rotate to ENU frame
        R_v2e = self.quat_to_rotmat(self.x.quat)
        acc_e = R_v2e @ acc_v
        
        # Add gravity
        acc_e += G
        
        # ---- State propagation ----
        # Position
        self.x.pos += self.x.vel * dt + 0.5 * acc_e * dt**2
        
        # Velocity
        self.x.vel += acc_e * dt
        
        # Quaternion kinematics
        # q_dot = 0.5 * q ⊗ [0, gyro_v]
        omega = np.array([0.0, gyro_v[0], gyro_v[1], gyro_v[2]])
        q_dot = 0.5 * self.quat_multiply(self.x.quat, omega)
        self.x.quat += q_dot * dt
        self.x.quat /= norm(self.x.quat)  # Normalize
        
        # Biases: random walk (no change in predict, only in covariance)
        
        # ---- Covariance propagation (F @ P @ F.T + Q) ----
        # Build F matrix (16x16) - linearized error state transition
        F = np.eye(16)
        
        # d(pos)/d(vel) = I * dt
        F[0:3, 3:6] = np.eye(3) * dt
        
        # d(vel)/d(quat) = -R * [acc_v]_x * dt
        acc_v_skew = self._skew_symmetric(acc_v)
        F[3:6, 6:10] = -R_v2e @ acc_v_skew * dt
        
        # d(vel)/d(acc_bias) = -R_v2e @ R_p2v * dt
        F[3:6, 10:13] = -R_v2e @ self.R_p2v * dt
        
        # d(quat)/d(gyro_bias) = -0.5 * d(q⊗[0,gyro])/d(gyro) * dt
        # = -0.5 * Q_left(q) * [0; I] * dt
        # Simplified: quat error due to gyro bias
        Q_left = self._quat_left_matrix(self.x.quat)
        F[6:10, 13:16] = -0.5 * Q_left[1:, 1:] * dt
        
        # Process noise Q (discrete)
        Q = np.zeros((16, 16))
        # Accel noise -> vel, pos
        Q[3:6, 3:6] = np.eye(3) * (self.q_acc**2) * dt
        Q[0:3, 0:3] = np.eye(3) * (self.q_acc**2) * dt**3 / 3
        Q[0:3, 3:6] = np.eye(3) * (self.q_acc**2) * dt**2 / 2
        Q[3:6, 0:3] = Q[0:3, 3:6].T
        
        # Gyro noise -> quat
        Q[6:10, 6:10] = np.eye(4) * (self.q_gyro**2) * dt  # approx
        
        # Bias random walks
        Q[10:13, 10:13] = np.eye(3) * (self.q_acc_bias**2) * dt
        Q[13:16, 13:16] = np.eye(3) * (self.q_gyro_bias**2) * dt
        
        # Propagate covariance
        self.P = F @ self.P @ F.T + Q
        
        # Ensure symmetry
        self.P = (self.P + self.P.T) * 0.5
    
    @staticmethod
    def _skew_symmetric(v: np.ndarray) -> np.ndarray:
        return np.array([
            [0, -v[2], v[1]],
            [v[2], 0, -v[0]],
            [-v[1], v[0], 0]
        ])
    
    @staticmethod
    def _quat_left_matrix(q: np.ndarray) -> np.ndarray:
        w, x, y, z = q
        return np.array([
            [w, -x, -y, -z],
            [x,  w, -z,  y],
            [y,  z,  w, -x],
            [z, -y,  x,  w]
        ])
    
    # ============================
    # MEASUREMENT UPDATES
    # ============================
    
    def update_ai_speed(self, ai: AISpeedData):
        """AI SpeedNet forward speed measurement (NHC: v_y=0, v_z=0)"""
        # Measurement: v_fwd = R_v2e[0, :] @ vel  (first row = forward axis)
        # But we already have speed in vehicle frame from SpeedNet
        # So H maps state to v_x (forward speed in vehicle frame)
        R_v2e = self.quat_to_rotmat(self.x.quat)
        
        # Innovation: z = v_ai - v_x
        v_pred = self.x.vel[0]  # forward velocity in vehicle frame (assuming vehicle x=forward)
        z = ai.speed - v_pred
        
        # H matrix: [0, 0, 0,  1, 0, 0,  0,0,0,0,  0,0,0,  0,0,0]
        H = np.zeros((1, 16))
        H[0, 3] = 1.0  # d(v_x)/d(vel_x) = 1
        
        # Measurement noise
        R = np.array([[ai.speed_std**2]])
        
        self._ekf_update(z, H, R)
        
        # NHC: Non-holonomic constraint (v_y=0, v_z=0 in vehicle frame)
        # Only apply if moving forward (speed > threshold)
        if ai.speed > 0.5:
            self._apply_nhc(ai.speed)
    
    def _apply_nhc(self, speed: float):
        """Apply NHC: lateral and vertical velocity = 0 in vehicle frame"""
        R_v2e = self.quat_to_rotmat(self.x.quat)
        
        # Velocity in vehicle frame
        vel_v = R_v2e.T @ self.x.vel
        
        # Innovation for NHC: z = [0, 0] - [v_y, v_z]
        z = np.array([-vel_v[1], -vel_v[2]])
        
        # H matrix for NHC: maps state to [v_y, v_z] in vehicle frame
        H = np.zeros((2, 16))
        # d(v_y)/d(vel) = R_v2e[1, :]
        # d(v_z)/d(vel) = R_v2e[2, :]
        H[0, 3:6] = R_v2e[1, :]
        H[1, 3:6] = R_v2e[2, :]
        
        # NHC noise (tight for lateral/vertical)
        R = np.diag([0.01**2, 0.01**2])  # 1 cm/s std
        
        self._ekf_update(z, H, R)
    
    def update_zupt(self, imu: IMUData) -> bool:
        """Zero-velocity update when stationary"""
        # Check if stationary
        acc_norm = norm(imu.acc - self.x.acc_bias)
        gyro_norm = norm(imu.gyro - self.x.gyro_bias)
        
        if acc_norm < self.zupt_acc_thresh and gyro_norm < self.zupt_gyro_thresh:
            # ZUPT measurement: v = 0
            z = -self.x.vel
            H = np.zeros((3, 16))
            H[:, 3:6] = np.eye(3)
            R = np.eye(3) * 0.001**2  # 1 mm/s std
            
            self._ekf_update(z, H, R)
            return True
        return False
    
    def update_gnss(self, gnss: GNSSData) -> bool:
        """GNSS position + velocity update with HDOP/sat gating"""
        # Gating
        if gnss.hdop > self.hdop_max or gnss.sats < self.sats_min:
            if not self.gnss_outage:
                self.gnss_outage = True
                self.outage_duration = 0.0
            return False
        
        # Recovery from outage
        if self.gnss_outage:
            self.gnss_outage = False
            # Re-seed check
            pos_innov = gnss.pos - self.x.pos
            pos_std = np.sqrt(np.diag(self.P[0:3, 0:3]))
            if np.any(np.abs(pos_innov) > self.innovation_gate * pos_std):
                # Hard re-seed
                self.x.pos = gnss.pos.copy()
                self.P[0:3, 0:3] = gnss.pos_cov.copy()
                print(f"GNSS re-seed: innovation {norm(pos_innov):.2f}m > gate")
            else:
                # Soft fusion (standard update)
                pass
            self.outage_duration = 0.0
        
        # Position update
        z_pos = gnss.pos - self.x.pos
        H_pos = np.zeros((3, 16))
        H_pos[:, 0:3] = np.eye(3)
        R_pos = gnss.pos_cov
        
        self._ekf_update(z_pos, H_pos, R_pos)
        
        # Velocity update
        z_vel = gnss.vel - self.x.vel
        H_vel = np.zeros((3, 16))
        H_vel[:, 3:6] = np.eye(3)
        R_vel = gnss.vel_cov
        
        self._ekf_update(z_vel, H_vel, R_vel)
        
        return True
    
    def update_map_match(self, mm: MapMatchData):
        """Map-matching position pseudo-measurement"""
        z = mm.pos - self.x.pos
        H = np.zeros((3, 16))
        H[:, 0:3] = np.eye(3)
        R = mm.pos_cov
        
        self._ekf_update(z, H, R)
    
    def _ekf_update(self, z: np.ndarray, H: np.ndarray, R: np.ndarray):
        """Standard EKF measurement update"""
        # Innovation covariance
        S = H @ self.P @ H.T + R
        
        # Kalman gain
        K = self.P @ H.T @ inv(S)
        
        # State update (error state)
        dx = K @ z
        
        # Apply error state to nominal state
        self.x.pos += dx[0:3]
        self.x.vel += dx[3:6]
        
        # Quaternion update: q = q ⊗ [1, 0.5*dtheta]
        dtheta = dx[6:9]  # small angle approx
        dq = np.array([1.0, dtheta[0]*0.5, dtheta[1]*0.5, dtheta[2]*0.5])
        self.x.quat = self.quat_multiply(self.x.quat, dq)
        self.x.quat /= norm(self.x.quat)
        
        self.x.acc_bias += dx[10:13]
        self.x.gyro_bias += dx[13:16]
        
        # Covariance update (Joseph form for numerical stability)
        I_KH = np.eye(16) - K @ H
        self.P = I_KH @ self.P @ I_KH.T + K @ R @ K.T
        self.P = (self.P + self.P.T) * 0.5
    
    # ============================
    # HIGH-LEVEL INTERFACE
    # ============================
    def step(self, imu: IMUData, gnss: Optional[GNSSData]=None, 
             ai: Optional[AISpeedData]=None, mm: Optional[MapMatchData]=None):
        """Single filter step"""
        self.predict(imu)
        
        if ai:
            self.update_ai_speed(ai)
        
        if gnss:
            self.update_gnss(gnss)
        else:
            self.outage_duration += imu.dt
        
        if mm:
            self.update_map_match(mm)
        
        # ZUPT check (always)
        self.update_zupt(imu)
        
        return self.x, self.P
    
    def get_state(self) -> Tuple[np.ndarray, np.ndarray]:
        """Return (pos, vel) in ENU"""
        return self.x.pos.copy(), self.x.vel.copy()
    
    def get_vehicle_velocity(self) -> np.ndarray:
        """Velocity in vehicle frame"""
        R_v2e = self.quat_to_rotmat(self.x.quat)
        return R_v2e.T @ self.x.vel
    
    def get_covariance_diag(self) -> np.ndarray:
        return np.diag(self.P)


# ============================
# TEST / DEMO
# ============================
if __name__ == "__main__":
    # Identity alignment for testing
    R_p2v = np.eye(3)
    ekf = DeadReckoningEKF(R_p2v)
    
    # Simulate 10s of stationary IMU
    print("Testing ZUPT on stationary...")
    for i in range(1000):  # 10s @ 100Hz
        imu = IMUData(
            acc=np.array([0.0, 0.0, -9.80665]) + np.random.normal(0, 0.01, 3),
            gyro=np.random.normal(0, 0.001, 3),
            dt=0.01,
            timestamp=i*0.01
        )
        ekf.step(imu)
    
    pos, vel = ekf.get_state()
    print(f"After 10s stationary: pos={pos}, vel={vel}")
    print(f"Pos std: {np.sqrt(ekf.P[0:3, 0:3].diagonal())}")
    print(f"Vel std: {np.sqrt(ekf.P[3:6, 3:6].diagonal())}")
    
    # Simulate constant velocity motion
    print("\nTesting constant velocity (5 m/s)...")
    for i in range(500):  # 5s
        imu = IMUData(
            acc=np.array([0.0, 0.0, -9.80665]) + np.random.normal(0, 0.02, 3),
            gyro=np.random.normal(0, 0.002, 3),
            dt=0.01,
            timestamp=10.0 + i*0.01
        )
        ai = AISpeedData(speed=5.0, speed_std=0.1, timestamp=10.0 + i*0.01)
        ekf.step(imu, ai=ai)
    
    pos, vel = ekf.get_state()
    print(f"After 5s motion: pos={pos}, vel={vel}")
    print(f"Vehicle vel: {ekf.get_vehicle_velocity()}")