[y, Fs] = audioread('sample.wav');
y_mono = mean(y, 2); % average stereo channels
audiowrite('sample_mono.wav', y_mono, Fs);
