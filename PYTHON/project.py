import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import soundfile as sf
import librosa

# -------------------------
# Bandpass Filter Design
# -------------------------
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs  # Nyquist Frequency
    low = lowcut / nyq
    high = highcut / nyq
    return butter(order, [low, high], btype='band')

def apply_filter(data, lowcut, highcut, fs, order=6):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

# -------------------------
# Load audio and filter
# -------------------------
 # auto-resamples to 16kHz
file_path = 'input.wav'
data, fs = sf.read(file_path)
print(fs) 


# Mono conversion if stereo
if len(data.shape) > 1:
    data = data.mean(axis=1)

# Filter parameters
lowcut = 300.0    # Lower frequency cutoff (Hz)
highcut = 3400.0  # Upper frequency cutoff (Hz)

filtered_data = 2*apply_filter(data, lowcut, highcut, fs)

# -------------------------
# Save output and plot
# -------------------------
sf.write('filtered.wav', filtered_data, fs)

# Plot before and after
plt.figure(figsize=(12, 6))
plt.subplot(2,1,1)
plt.title("Original Signal")
plt.plot(data, color='gray')
plt.subplot(2,1,2)
plt.title("Filtered Signal (Bandpass 300–3400Hz)")
plt.plot(filtered_data, color='blue')
plt.tight_layout()
plt.show()
