clc, clear, clearvars;

[datain,fs]=audioread("project.wav");
dataout= 2*filter(bpfilter_design,datain);
audiowrite("filtered.wav",dataout,fs)