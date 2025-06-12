# Audiofilter-denoise-matlab-python
Audio denoising using bandpass filtering in MATLAB and Python. A simple project focused on reducing noise in speech signals through frequency-based filtering. The main focus is on applying a **bandpass filter** to enhance speech signals and remove unwanted frequency components.


## 📁 Contents

- MATLAB script to apply a bandpass filter to a `.wav` file.
- Python script using `librosa`, `scipy`, and `matplotlib` for filtering and visualizing audio.
- Input: `project.wav`
- Output: `filtered.wav` (MATLAB) / `filtered_speech.wav` (Python)

---

## 📌 Features

### ✅ Common
- Loads and processes WAV audio files
- Applies bandpass filtering to isolate speech range
- Saves the filtered result to disk

### 🧪 Python-Specific
- Resamples audio to 16kHz(*** used just as an application of librosa library instead use "data, fs = sf.read(file_path)"  gives fs=44100 ***)
- Designs nth-order Butterworth filter (desired frequency range generally 300-3400 Hz for speech signals )
- Applies zero-phase filtering (`filtfilt`)(
✅ Use `filtfilt` for speech/audio/EEG denoising, no phase distortion
✅ Use `lfilter` for real-time systems or when delay is acceptable)
- Normalizes audio
- Plots detailed **before/after spectrograms**
- (Commented) FFT spectrum analysis

### 🧪 MATLAB-Specific
- Uses a predefined bandpass filter (`bpfilter_design` usihg matlab builtin filterdesign gui)
- Filters `project.wav` and writes `filtered.wav`
- `stereo_mono.m` to convert my stereo `project.wav` file to mono type.

---

## 🛠 Requirements

### MATLAB
- MATLAB R2020 or later
- Signal Processing Toolbox

### Python
- Python 3.8+
- `numpy`
- `scipy`
- `matplotlib`
- `librosa`
- `soundfile`

Install with:
```bash
pip install numpy scipy matplotlib librosa soundfile

