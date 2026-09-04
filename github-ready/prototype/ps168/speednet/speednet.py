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