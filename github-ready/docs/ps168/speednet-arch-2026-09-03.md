# SIH26168 — SpeedNet Architecture (Exact Production Config)

> **Purpose:** CNN + BiLSTM speed estimator from IMU → ONNX → TFLite INT8 for mobile/edge
> **Input:** 2s window @ 100Hz, 6 IMU channels (ax, ay, az, gx, gy, gz) → **Output:** forward speed [m/s]
> **Dataset:** IO-VNBD (phone 10Hz → upsample, car 100Hz) + augmentation

---

## Architecture (PyTorch)

```python
# /Users/shreyashsingh/my info/projects/sih26/prototype/speednet/speednet.py
import torch
import torch.nn as nn
import torch.nn.functional as F

class SpeedNet(nn.Module):
    """
    SpeedNet: 1D-CNN + BiLSTM for forward speed estimation from IMU
    Input: (batch, 200, 6)  # 2 seconds @ 100Hz, 6 channels
    Output: (batch, 1)      # forward speed [m/s]
    Total params: ~180K (mobile-friendly)
    """
    
    def __init__(self, input_channels=6, seq_len=200, hidden_dim=64, dropout=0.3):
        super().__init__()
        self.input_channels = input_channels
        self.seq_len = seq_len
        self.hidden_dim = hidden_dim
        
        # 1D CNN Feature Extractor
        self.conv1 = nn.Sequential(
            nn.Conv1d(input_channels, 32, kernel_size=7, stride=1, padding=3, bias=False),
            nn.BatchNorm1d(32),
            nn.ReLU(inplace=True)
        )
        self.conv2 = nn.Sequential(
            nn.Conv1d(32, 64, kernel_size=7, stride=1, padding=3, bias=False),
            nn.BatchNorm1d(64),
            nn.ReLU(inplace=True)
        )
        self.conv3 = nn.Sequential(
            nn.Conv1d(64, 128, kernel_size=7, stride=1, padding=3, bias=False),
            nn.BatchNorm1d(128),
            nn.ReLU(inplace=True)
        )
        
        # BiLSTM for temporal modeling
        self.lstm = nn.LSTM(
            input_size=128,
            hidden_size=hidden_dim,
            num_layers=1,
            batch_first=True,
            bidirectional=True,
            dropout=0.0
        )
        
        # Dropout
        self.dropout = nn.Dropout(dropout)
        
        # Regression head
        self.fc = nn.Linear(hidden_dim * 2, 1)  # *2 for bidirectional
        
        # Initialize weights
        self._init_weights()
    
    def _init_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv1d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm1d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.LSTM):
                for name, param in m.named_parameters():
                    if 'weight_ih' in name:
                        nn.init.xavier_uniform_(param)
                    elif 'weight_hh' in name:
                        nn.init.orthogonal_(param)
                    elif 'bias' in name:
                        nn.init.constant_(param, 0)
            elif isinstance(m, nn.Linear):
                nn.init.xavier_uniform_(m.weight)
                nn.init.constant_(m.bias, 0)
    
    def forward(self, x):
        """
        x: (batch, seq_len, channels) -> (batch, 200, 6)
        """
        # Transpose for Conv1d: (batch, channels, seq_len)
        x = x.transpose(1, 2)  # (batch, 6, 200)
        
        # CNN feature extraction
        x = self.conv1(x)   # (batch, 32, 200)
        x = self.conv2(x)   # (batch, 64, 200)
        x = self.conv3(x)   # (batch, 128, 200)
        
        # Transpose back for LSTM: (batch, seq_len, features)
        x = x.transpose(1, 2)  # (batch, 200, 128)
        
        # BiLSTM
        lstm_out, _ = self.lstm(x)  # (batch, 200, hidden_dim*2)
        
        # Use last timestep output
        x = lstm_out[:, -1, :]  # (batch, hidden_dim*2)
        
        # Dropout + regression
        x = self.dropout(x)
        x = self.fc(x)  # (batch, 1)
        
        return x.squeeze(-1)  # (batch,)

    def count_parameters(self):
        return sum(p.numel() for p in self.parameters() if p.requires_grad)


def get_model(device='cpu'):
    model = SpeedNet()
    print(f"SpeedNet parameters: {model.count_parameters():,}")
    return model.to(device)


if __name__ == "__main__":
    model = get_model()
    # Test forward pass
    x = torch.randn(4, 200, 6)
    y = model(x)
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {y.shape}")
    print(f"Output range: [{y.min().item():.3f}, {y.max().item():.3f}] m/s")
```

---

## Training Configuration

```python
# /Users/shreyashsingh/my info/projects/sih26/prototype/speednet/train.py
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
from speednet import SpeedNet
import os

# Hyperparameters
CONFIG = {
    "batch_size": 256,
    "epochs": 50,
    "lr": 1e-3,
    "weight_decay": 1e-5,
    "patience": 10,
    "device": "cuda" if torch.cuda.is_available() else "cpu",
    "seed": 42,
}

torch.manual_seed(CONFIG["seed"])
np.random.seed(CONFIG["seed"])

# Loss: MSE + 0.1 * MAE (robust to outliers)
class CombinedLoss(nn.Module):
    def __init__(self, alpha=0.1):
        super().__init__()
        self.alpha = alpha
        self.mse = nn.MSELoss()
        self.mae = nn.L1Loss()
    
    def forward(self, pred, target):
        return self.mse(pred, target) + self.alpha * self.mae(pred, target)


def train_one_epoch(model, loader, optimizer, criterion, device):
    model.train()
    total_loss = 0
    for imu, speed in loader:
        imu, speed = imu.to(device), speed.to(device)
        optimizer.zero_grad()
        pred = model(imu)
        loss = criterion(pred, speed)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        total_loss += loss.item() * imu.size(0)
    return total_loss / len(loader.dataset)


def validate(model, loader, criterion, device):
    model.eval()
    total_loss = 0
    preds, targets = [], []
    with torch.no_grad():
        for imu, speed in loader:
            imu, speed = imu.to(device), speed.to(device)
            pred = model(imu)
            loss = criterion(pred, speed)
            total_loss += loss.item() * imu.size(0)
            preds.append(pred.cpu())
            targets.append(speed.cpu())
    preds = torch.cat(preds)
    targets = torch.cat(targets)
    mae = torch.abs(preds - targets).mean().item()
    rmse = torch.sqrt(torch.mean((preds - targets) ** 2)).item()
    return total_loss / len(loader.dataset), mae, rmse


def main():
    # Load preprocessed IO-VNBD data (from Task 1D)
    # Expected: X_train (N, 200, 6), y_train (N,), X_val, y_val, X_test, y_test
    data = np.load("io_vnbd_processed.npz")
    X_train, y_train = data["X_train"], data["y_train"]
    X_val, y_val = data["X_val"], data["y_val"]
    X_test, y_test = data["X_test"], data["y_test"]
    
    print(f"Train: {X_train.shape}, Val: {X_val.shape}, Test: {X_test.shape}")
    
    # DataLoaders
    train_ds = TensorDataset(torch.FloatTensor(X_train), torch.FloatTensor(y_train))
    val_ds = TensorDataset(torch.FloatTensor(X_val), torch.FloatTensor(y_val))
    test_ds = TensorDataset(torch.FloatTensor(X_test), torch.FloatTensor(y_test))
    
    train_loader = DataLoader(train_ds, batch_size=CONFIG["batch_size"], shuffle=True, num_workers=4)
    val_loader = DataLoader(val_ds, batch_size=CONFIG["batch_size"], shuffle=False, num_workers=4)
    test_loader = DataLoader(test_ds, batch_size=CONFIG["batch_size"], shuffle=False, num_workers=4)
    
    # Model, optimizer, scheduler
    model = SpeedNet().to(CONFIG["device"])
    optimizer = torch.optim.AdamW(model.parameters(), lr=CONFIG["lr"], weight_decay=CONFIG["weight_decay"])
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=CONFIG["epochs"])
    criterion = CombinedLoss(alpha=0.1)
    
    # Training loop
    best_val_loss = float('inf')
    patience_counter = 0
    
    for epoch in range(CONFIG["epochs"]):
        train_loss = train_one_epoch(model, train_loader, optimizer, criterion, CONFIG["device"])
        val_loss, val_mae, val_rmse = validate(model, val_loader, criterion, CONFIG["device"])
        scheduler.step()
        
        print(f"Epoch {epoch:3d} | Train: {train_loss:.6f} | Val: {val_loss:.6f} | MAE: {val_mae:.4f} | RMSE: {val_rmse:.4f}")
        
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            torch.save(model.state_dict(), "speednet_best.pth")
            print("  → Saved best model")
        else:
            patience_counter += 1
            if patience_counter >= CONFIG["patience"]:
                print(f"Early stopping at epoch {epoch}")
                break
    
    # Final test evaluation
    model.load_state_dict(torch.load("speednet_best.pth"))
    test_loss, test_mae, test_rmse = validate(model, test_loader, criterion, CONFIG["device"])
    print(f"\nTEST | Loss: {test_loss:.6f} | MAE: {test_mae:.4f} m/s | RMSE: {test_rmse:.4f} m/s")
    
    # Export ONNX
    export_onnx(model, CONFIG["device"])


def export_onnx(model, device):
    model.eval()
    dummy = torch.randn(1, 200, 6, device=device)
    torch.onnx.export(
        model, dummy, "speednet.onnx",
        input_names=["imu"],
        output_names=["speed"],
        dynamic_axes={"imu": {0: "batch"}, "speed": {0: "batch"}},
        opset_version=14,
        do_constant_folding=True
    )
    print("Exported speednet.onnx")
    
    # Verify ONNX
    import onnx
    onnx_model = onnx.load("speednet.onnx")
    onnx.checker.check_model(onnx_model)
    print("ONNX model valid")


if __name__ == "__main__":
    main()
```

---

## ONNX Export + TFLite INT8 Quantization

```python
# /Users/shreyashsingh/my info/projects/sih26/prototype/speednet/export_onnx.py
import torch
import onnx
from speednet import SpeedNet

def export():
    model = SpeedNet()
    model.load_state_dict(torch.load("speednet_best.pth", map_location="cpu"))
    model.eval()
    
    dummy = torch.randn(1, 200, 6)
    torch.onnx.export(
        model, dummy, "speednet.onnx",
        input_names=["imu"],
        output_names=["speed"],
        dynamic_axes={"imu": {0: "batch"}, "speed": {0: "batch"}},
        opset_version=14,
        do_constant_folding=True
    )
    
    onnx_model = onnx.load("speednet.onnx")
    onnx.checker.check_model(onnx_model)
    print("speednet.onnx exported and verified")
    
    # Print model info
    print(f"Input: {onnx_model.graph.input[0].name} {onnx_model.graph.input[0].type.tensor_type.shape.dim}")
    print(f"Output: {onnx_model.graph.output[0].name} {onnx_model.graph.output[0].type.tensor_type.shape.dim}")

if __name__ == "__main__":
    export()
```

```python
# /Users/shreyashsingh/my info/projects/sih26/prototype/speednet/quantize_tflite.py
import tensorflow as tf
import numpy as np
from speednet import SpeedNet
import torch

def representative_dataset_gen():
    """Yield 100 calibration samples from validation set"""
    data = np.load("io_vnbd_processed.npz")
    X_val = data["X_val"][:100]  # (100, 200, 6)
    for i in range(len(X_val)):
        yield [X_val[i:i+1].astype(np.float32)]

def quantize():
    # Convert ONNX → TFLite with INT8 quantization
    converter = tf.lite.TFLiteConverter.from_onnx("speednet.onnx")
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.target_spec.supported_ops = [
        tf.lite.OpsSet.TFLITE_BUILTINS_INT8,
        tf.lite.OpsSet.SELECT_TF_OPS  # fallback if needed
    ]
    converter.inference_input_type = tf.int8
    converter.inference_output_type = tf.int8
    converter.representative_dataset = representative_dataset_gen
    
    tflite_model = converter.convert()
    
    with open("speednet_int8.tflite", "wb") as f:
        f.write(tflite_model)
    
    print(f"TFLite INT8 model size: {len(tflite_model) / 1024:.1f} KB")
    
    # Verify inference
    interpreter = tf.lite.Interpreter(model_content=tflite_model)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    print(f"Input: {input_details[0]['name']} {input_details[0]['shape']} {input_details[0]['dtype']}")
    print(f"Output: {output_details[0]['name']} {output_details[0]['shape']} {output_details[0]['dtype']}")
    
    # Test with random input
    test_input = np.random.randn(1, 200, 6).astype(np.float32)
    # Quantize input
    input_scale, input_zero_point = input_details[0]['quantization']
    test_input_q = (test_input / input_scale + input_zero_point).astype(np.int8)
    
    interpreter.set_tensor(input_details[0]['index'], test_input_q)
    interpreter.invoke()
    output_q = interpreter.get_tensor(output_details[0]['index'])
    
    # Dequantize output
    output_scale, output_zero_point = output_details[0]['quantization']
    output = (output_q.astype(np.float32) - output_zero_point) * output_scale
    print(f"Test inference: {output[0][0]:.3f} m/s")

if __name__ == "__main__":
    quantize()
```

---

## Data Augmentation Pipeline (for training)

```python
# /Users/shreyashsingh/my info/projects/sih26/prototype/speednet/augment.py
import numpy as np
import random

def augment_imu(imu, speed, aug_prob=0.5):
    """
    imu: (200, 6) - 2s @ 100Hz
    speed: scalar [m/s]
    """
    imu = imu.copy()
    
    if random.random() < aug_prob:
        # Gaussian noise (sensor noise)
        noise_std = 0.01  # ~1% of typical accel/gyro
        imu += np.random.normal(0, noise_std, imu.shape)
    
    if random.random() < aug_prob:
        # Random rotation (phone orientation variance)
        # Small rotation around gravity axis (yaw)
        angle = np.random.uniform(-0.2, 0.2)  # ~±11 deg
        ca, sa = np.cos(angle), np.sin(angle)
        R = np.array([[ca, -sa, 0], [sa, ca, 0], [0, 0, 1]])
        # Apply to accel (0:3) and gyro (3:6)
        imu[:, :3] = imu[:, :3] @ R.T
        imu[:, 3:] = imu[:, 3:] @ R.T
    
    if random.random() < aug_prob:
        # Shock impulse (pothole)
        idx = random.randint(50, 150)
        imu[idx:idx+5, :3] += np.random.normal(0, 2.0, (5, 3))  # ±2g spike
    
    if random.random() < aug_prob:
        # Time stretch (speed variation)
        factor = random.uniform(0.9, 1.1)
        new_len = int(200 * factor)
        from scipy.interpolate import interp1d
        x_old = np.linspace(0, 1, 200)
        x_new = np.linspace(0, 1, new_len)
        for ch in range(6):
            f = interp1d(x_old, imu[:, ch], kind='linear')
            imu[:, ch] = f(x_new)
        # Interpolate back to 200
        if new_len != 200:
            for ch in range(6):
                f = interp1d(np.linspace(0, 1, new_len), imu[:, ch], kind='linear')
                imu[:, ch] = f(x_old)
        speed *= factor
    
    if random.random() < aug_prob:
        # Channel dropout (simulate sensor failure)
        ch = random.randint(0, 5)
        imu[:, ch] = 0
    
    return imu, speed


def prepare_training_data(X, y, augment_factor=3):
    """Expand dataset with augmentations"""
    X_aug, y_aug = [X], [y]
    for _ in range(augment_factor - 1):
        X_batch, y_batch = [], []
        for i in range(len(X)):
            xi, yi = augment_imu(X[i], y[i])
            X_batch.append(xi)
            y_batch.append(yi)
        X_aug.append(np.array(X_batch))
        y_aug.append(np.array(y_batch))
    return np.concatenate(X_aug), np.concatenate(y_aug)
```

---

## Benchmark Results (Expected)

| Metric | Target | Notes |
|---|---|---|
| **Params** | ~180K | Mobile-friendly |
| **MAE (val)** | < 0.15 m/s | On IO-VNBD test split |
| **RMSE (val)** | < 0.25 m/s | |
| **ONNX size** | ~700 KB | FP32 |
| **TFLite INT8 size** | ~180 KB | 4× compression |
| **Latency (CPU)** | < 10 ms | Snapdragon 8 Gen 2 |
| **Latency (TFLite)** | < 5 ms | INT8 |

---

## Files Created

| File | Path |
|---|---|
| Model definition | `projects/sih26/prototype/speednet/speednet.py` |
| Training script | `projects/sih26/prototype/speednet/train.py` |
| ONNX export | `projects/sih26/prototype/speednet/export_onnx.py` |
| TFLite quantization | `projects/sih26/prototype/speednet/quantize_tflite.py` |
| Augmentation | `projects/sih26/prototype/speednet/augment.py` |
| This spec | `reference/research/sih26/speednet-arch-2026-09-03.md` |

---

## Next Steps
1. `cd projects/sih26/prototype/speednet`
2. `pip install torch onnx onnxruntime tensorflow`
3. Prepare `io_vnbd_processed.npz` from Task 1D
4. `python train.py`
5. `python export_onnx.py`
6. `python quantize_tflite.py`
7. Verify `speednet_int8.tflite` < 200 KB, MAE < 0.15 m/s