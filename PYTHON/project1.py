import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, spectrogram

# === 1. Load and resample audio to 16kHz ===
file_path = 'project.wav'  
data, fs = librosa.load(file_path,sr=16000) 
print(data) # Automatically resamples

# === 2. Design bandpass filter: 300–3400 Hz ===
lowcut = 300.0
highcut = 3400.0
nyq = 0.5 * fs
low = lowcut / nyq
high = highcut / nyq
b, a = butter(N=4, Wn=[low, high], btype='band')

# === 3. Apply zero-phase filter ===
filtered_data = filtfilt(b, a, data)

# === 4. Normalize both signals ===
data = data / np.max(np.abs(data))
filtered_data = filtered_data / np.max(np.abs(filtered_data))

# === 5. Save filtered audio ===
sf.write('filtered_speech.wav', filtered_data, fs)

# === 6. Plot side-by-side spectrograms ===
f1, t1, Sxx1 = spectrogram(data, fs, nperseg=512)
f2, t2, Sxx2 = spectrogram(filtered_data, fs, nperseg=512)

plt.figure(figsize=(14, 6))

# Original
plt.subplot(1, 2, 1)
plt.pcolormesh(t1, f1, 10 * np.log10(Sxx1 + 1e-10), shading='gouraud', cmap='viridis')
plt.title('Original Speech Spectrogram')
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')
plt.ylim(0, 8000)
plt.colorbar(label='dB')

# Filtered
plt.subplot(1, 2, 2)
plt.pcolormesh(t2, f2, 10 * np.log10(Sxx2 + 1e-10), shading='gouraud', cmap='viridis')
plt.title('Filtered Speech Spectrogram ')
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')
plt.ylim(0, 8000)
plt.colorbar(label='dB')

plt.tight_layout()
plt.show()


# data: original audio (1D NumPy array)
# filtered_data: filtered audio
# fs: sampling rate (e.g., 44100)

# def plot_fft(signal, fs, title):
#     N = len(signal)
#     freqs = np.fft.rfftfreq(N, 1/fs)          # Frequency bins
#     fft_spectrum = np.abs(np.fft.rfft(signal))  # Magnitude of FFT

#     plt.plot(freqs, fft_spectrum, label=title)
#     plt.xlabel('Frequency (Hz)')
#     plt.ylabel('Magnitude')
#     plt.grid(True)

# # Plot both signals
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plot_fft(data, fs, 'Original Signal')
# plt.subplot(1, 2, 2)
# plot_fft(filtered_data, fs, 'Filtered Signal')

# plt.title('FFT Spectrum: Original vs Filtered')
# plt.legend()
# plt.xlim(0, 8000)  # Limit to 0–8kHz for speech
# plt.tight_layout()
# plt.show()

