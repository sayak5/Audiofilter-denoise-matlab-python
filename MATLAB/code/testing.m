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