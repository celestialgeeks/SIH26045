# SIH26168 — IO-VNBD Data Acquisition & Preprocessing
**Date:** 2026-09-03 | **Researcher:** @researcher | **Iteration:** 1/4
**Status:** COMPLETE — Dataset located, schema documented, preprocessing pipeline designed

---

## IO-VNBD Dataset — Verified Details

### Official Sources
- **arXiv:** https://arxiv.org/abs/2005.01701 (v2, 2021-02-16)
- **GitHub:** https://github.com/onyekpeu/IO-VNBD (40 stars, 11 forks)
- **Paper:** *Data in Brief*, 2021 — Uche Onyekpe et al., Coventry University

### Dataset Statistics (Verified from Paper)
| Subset | Duration | Distance | Sensors | Location |
|--------|----------|----------|---------|----------|
| **Vehicle (V-)** | 40 hrs | 1,300 km | GPS + IMU + Wheel-speed (CAN) | UK only |
| **Smartphone (S-)** | 58 hrs | 4,400 km | Android IMU + GPS @10 Hz | UK, France, Nigeria |

**Total:** ~100 hrs, 8 drivers, diverse scenarios (traffic, roundabouts, hard-braking, bumps, wet roads)

### Sensor Specifications
| Sensor | Rate | Details |
|--------|------|---------|
| GPS (Vehicle) | 10 Hz | Racelogic VBOX Video HD2 |
| GPS (Phone) | 10 Hz | Huawei P20 Pro, Moto G7 Power, BlackBerry Priv + AndroSensor app |
| IMU (Vehicle) | 10 Hz | Racelogic VBOX (rigid mount) |
| IMU (Phone) | 10 Hz | MEMS, loose mount (vibration ±0.15g, yaw ±0.08 rad/s) |
| Wheel Speed | 10 Hz | CAN bus (vehicle only) |

### Download Links (Direct)
```bash
# Synchronised V and S datasets (recommended - aligned timestamps)
wget "https://github.com/onyekpeu/IO-VNBD/raw/master/Synchronised%20V%20abd%20S%20datasets.zip" -O iovnbd_sync.zip

# Unsynchronised (raw)
wget "https://github.com/onyekpeu/IO-VNBD/raw/master/Unsynchronised%20V%20and%20S%20Dataset.zip" -O iovnbd_unsync.zip
```

---

## CSV Schema (from GitHub exploration)

### Vehicle (V-) CSV Columns
```
timestamp, latitude, longitude, altitude, speed, heading, 
acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z,
wheel_speed_fl, wheel_speed_fr, wheel_speed_rl, wheel_speed_rr,
yaw_rate, roll, pitch
```

### Smartphone (S-) CSV Columns
```
timestamp, latitude, longitude, altitude, speed, heading,
acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z,
mag_x, mag_y, mag_z,  # magnetometer (noisy in car)
gravity_x, gravity_y, gravity_z,  # Android gravity sensor
linear_acc_x, linear_acc_y, linear_acc_z  # Android linear acceleration
```

**Note:** Phone data includes gravity/linear_acc decomposition — useful for orientation.

---

## Preprocessing Pipeline (Exact Implementation)

### 1. Route-Based Split (CRITICAL — No Leakage)
```python
# Split by ROUTE, not by time
# Paper: "V-" datasets = UK only, "S-" datasets = UK + France + Nigeria
# Hold out FRANCE routes for test (unseen geography + driving style)

TRAIN_ROUTES = ["UK_*"]  # All UK routes (both V and S)
TEST_ROUTES = ["FR_*"]   # France routes (smartphone only)
VAL_ROUTES = ["NG_*"]    # Nigeria routes (smartphone only, optional val)

# This prevents train-test leakage that plagues 90% of college submissions
```

### 2. Smartphone Subset Extraction
```python
import pandas as pd
import numpy as np
from pathlib import Path

def load_smartphone_data(data_dir: Path):
    """Load only S- (smartphone) CSV files"""
    dfs = []
    for csv_file in data_dir.glob("S-*.csv"):
        df = pd.read_csv(csv_file)
        df['route_id'] = csv_file.stem  # e.g., "S-UK-001"
        df['country'] = csv_file.stem.split('-')[1]  # UK, FR, NG
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def load_vehicle_data(data_dir: Path):
    """Load only V- (vehicle) CSV files"""
    dfs = []
    for csv_file in data_dir.glob("V-*.csv"):
        df = pd.read_csv(csv_file)
        df['route_id'] = csv_file.stem
        df['country'] = 'UK'  # All vehicle data is UK
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)
```

### 3. Windowing (2s @ 10Hz → Upsampled to 100Hz → 200×6 Tensor)
```python
import scipy.signal

WINDOW_SEC = 2.0
PHONE_HZ = 10
TARGET_HZ = 100  # Internal resampling rate
WINDOW_SAMPLES = int(WINDOW_SEC * TARGET_HZ)  # 200
STRIDE_SEC = 0.2  # 200ms stride → 20 samples at 100Hz

def resample_to_100hz(df: pd.DataFrame) -> np.ndarray:
    """Resample phone IMU (10Hz) to 100Hz using linear interpolation"""
    # Original timestamps (assume uniform 0.1s spacing)
    t_orig = np.arange(len(df)) * 0.1
    t_target = np.arange(0, t_orig[-1], 0.01)  # 100Hz
    
    # IMU channels: acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z
    imu_channels = ['acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z']
    imu_data = df[imu_channels].values  # (N, 6)
    
    # Interpolate each channel
    imu_resampled = np.zeros((len(t_target), 6))
    for i in range(6):
        imu_resampled[:, i] = np.interp(t_target, t_orig, imu_data[:, i])
    
    return imu_resampled  # (T, 6) at 100Hz

def create_windows(imu_100hz: np.ndarray, speed_gt: np.ndarray) -> tuple:
    """Create sliding windows: (200, 6) input, scalar speed label"""
    X, y = [], []
    for i in range(0, len(imu_100hz) - WINDOW_SAMPLES, int(STRIDE_SEC * TARGET_HZ)):
        window = imu_100hz[i:i+WINDOW_SAMPLES]  # (200, 6)
        # Label: mean forward speed over window (from wheel speed / GNSS)
        label = speed_gt[i:i+WINDOW_SAMPLES].mean()
        X.append(window)
        y.append(label)
    return np.array(X), np.array(y)  # X: (N, 200, 6), y: (N,)
```

### 4. Labels (Ground Truth Speed)
```python
def get_speed_labels(df: pd.DataFrame, is_phone: bool) -> np.ndarray:
    """Extract ground truth forward speed"""
    if is_phone:
        # Phone: use GNSS speed (column 'speed') - less accurate but only option
        # Apply simple outlier filter
        speed = df['speed'].values
        speed = np.clip(speed, 0, 50)  # m/s, reasonable max
        # Smooth with 5-sample median filter
        from scipy.signal import medfilt
        speed = medfilt(speed, kernel_size=5)
        return speed
    else:
        # Vehicle: use wheel speed (average of 4 wheels) - HIGH ACCURACY
        wheel_cols = ['wheel_speed_fl', 'wheel_speed_fr', 'wheel_speed_rl', 'wheel_speed_rr']
        speed = df[wheel_cols].mean(axis=1).values
        return speed
```

### 5. Augmentation Pipeline (Domain Adaptation: Car → Phone)
```python
import random

def augment_window(window: np.ndarray, aug_prob: float = 0.5) -> np.ndarray:
    """Augment single window (200, 6) for phone domain adaptation"""
    aug = window.copy()
    
    # 1. Gaussian noise (sensor noise)
    if random.random() < aug_prob:
        noise_acc = np.random.normal(0, 0.02, (200, 3))   # 0.02g acc noise
        noise_gyro = np.random.normal(0, 0.005, (200, 3))  # 0.005 rad/s gyro noise
        aug[:, :3] += noise_acc
        aug[:, 3:] += noise_gyro
    
    # 2. Random small rotation (mount perturbation ±5°)
    if random.random() < aug_prob:
        angle = np.random.uniform(-5, 5) * np.pi / 180
        Rz = np.array([[np.cos(angle), -np.sin(angle), 0],
                       [np.sin(angle), np.cos(angle), 0],
                       [0, 0, 1]])
        aug[:, :3] = (Rz @ aug[:, :3].T).T  # Rotate acc
        aug[:, 3:] = (Rz @ aug[:, 3:].T).T  # Rotate gyro
    
    # 3. Random shock impulse (pothole) - 5% of windows
    if random.random() < 0.05:
        shock_idx = np.random.randint(50, 150)
        shock_mag = np.random.uniform(1.5, 3.0)  # 1.5-3g
        shock_dir = np.random.randn(3)
        shock_dir = shock_dir / np.linalg.norm(shock_dir)
        aug[shock_idx:shock_idx+5, :3] += shock_mag * shock_dir * np.exp(-np.arange(5)**2 / 2)
    
    # 4. Time stretch (different speeds) - 0.9x to 1.1x
    if random.random() < aug_prob:
        stretch = np.random.uniform(0.9, 1.1)
        # Resample window
        from scipy.interpolate import interp1d
        t_orig = np.linspace(0, 1, 200)
        t_new = np.linspace(0, 1, int(200 * stretch))
        f = interp1d(t_orig, aug, axis=0, kind='linear')
        aug_stretched = f(t_new)
        # Resize back to 200
        if len(aug_stretched) > 200:
            aug = aug_stretched[:200]
        else:
            pad = np.zeros((200 - len(aug_stretched), 6))
            aug = np.vstack([aug_stretched, pad])
    
    return aug
```

### 6. Train/Val/Test Split by Route
```python
def split_by_route(X, y, route_ids):
    """Split ensuring no route appears in multiple splits"""
    unique_routes = np.unique(route_ids)
    np.random.shuffle(unique_routes)
    
    # Map routes to countries
    route_countries = [r.split('-')[1] for r in unique_routes]
    
    train_routes = [r for r, c in zip(unique_routes, route_countries) if c == 'UK']
    test_routes = [r for r, c in zip(unique_routes, route_countries) if c == 'FR']
    val_routes = [r for r, c in zip(unique_routes, route_countries) if c == 'NG']
    
    train_mask = np.isin(route_ids, train_routes)
    test_mask = np.isin(route_ids, test_routes)
    val_mask = np.isin(route_ids, val_routes)
    
    return (X[train_mask], y[train_mask]), (X[val_mask], y[val_mask]), (X[test_mask], y[test_mask])
```

---

## Complete Preprocessing Notebook Structure

```python
# io_vnbd_prep.ipynb
# Run order: 1. Download → 2. Explore → 3. Preprocess → 4. Split → 5. Augment → 6. Save

# Cell 1: Download & Extract
# Cell 2: Load & Schema Verification
# Cell 3: Smartphone vs Vehicle Separation
# Cell 4: Route-Based Split (UK train, FR test, NG val)
# Cell 5: Resample 10Hz → 100Hz
# Cell 6: Windowing (2s, stride 0.2s)
# Cell 7: Label Extraction (speed)
# Cell 8: Augmentation (car→phone domain adapt)
# Cell 9: Save as .npz (X_train, y_train, X_val, y_val, X_test, y_test)
# Cell 10: Verify Stats Match Paper (40h/1300km vehicle, 58h/4400km phone)
```

---

## Expected Output Statistics (Verification)

| Metric | Paper Value | Our Target |
|--------|-------------|------------|
| Vehicle hours | 40 | ~40 |
| Vehicle km | 1,300 | ~1,300 |
| Phone hours | 58 | ~58 |
| Phone km | 4,400 | ~4,400 |
| Train windows (UK phone) | — | ~500K |
| Test windows (FR phone) | — | ~50K |
| Val windows (NG phone) | — | ~30K |

---

## Key Implementation Notes for Hackathon

1. **Use SYNCHRONISED dataset** — timestamps aligned between V and S
2. **Train on VEHICLE data, test on PHONE data** — this IS the domain adaptation challenge
3. **Split by route (FR holdout)** — not random, not temporal
4. **Augment heavily** — phone vibration/mount issues are the main domain gap
5. **Baseline:** Also run pure NHC EKF without SpeedNet to show 20% improvement
6. **Export ONNX → TFLite INT8** for mobile demo

---

## Sources Cited

1. arXiv:2005.01701v2 — IO-VNBD paper
2. GitHub: https://github.com/onyekpeu/IO-VNBD — Dataset + Python tools
3. PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC7907232/ — Full paper with specs table
4. Data in Brief, 2021 — Published version