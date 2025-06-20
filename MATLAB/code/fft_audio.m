clc, clear, clearvars;

[datain,fs]=audioread("project.wav");
[n,p]=size(datain);
ts=1/fs;

tmax = (n-1)*ts;
t=0:ts:tmax;
plot(t,datain)
f=-fs/2:fs/(n-1):fs/2;
z=fftshift(fft(datain));
plot(f,abs(z))
function Hd = bpfilter_design
%BPFILTER_DESIGN Returns a discrete-time filter object.

% MATLAB Code
% Generated by MATLAB(R) 24.1 and Signal Processing Toolbox 24.1.
% Generated on: 05-Jun-2025 10:18:39

% Butterworth Bandpass filter designed using FDESIGN.BANDPASS.

% All frequency values are in Hz.
Fs = 44100;  % Sampling Frequency

N   = 10;    % Order
Fc1 = 300;   % First Cutoff Frequency
Fc2 = 3400;  % Second Cutoff Frequency

% Construct an FDESIGN object and call its BUTTER method.
h  = fdesign.bandpass('N,F3dB1,F3dB2', N, Fc1, Fc2, Fs);
Hd = design(h, 'butter');
end
% [EOF]


