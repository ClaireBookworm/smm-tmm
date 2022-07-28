cd '/Users/wanyilyu/Dropbox (Partners HealthCare)/Work from home/WolfeLab Experiments/Spatial Massive Memory - SMM/SMM_TMM/Result and analysis/Analysis_WL'

clear all

files = dir('*.xlsx');
thisData = readtable(files.name);
thisData = readtable('SMMTMM_23Os_withScreenSize.xlsx');
GoodOs = [5:7, 9:16, 19:23];

%% Probability in ROI across Log2Lag

