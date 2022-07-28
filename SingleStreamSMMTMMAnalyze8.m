% v6 cleans up the names of the simulated time error and computes it two
% different ways.
% also we output single simulated values for each trial so we can look at
% predicted correlations

%clear everything before you begin
clear all;
close all
%set the state of the random number generator to some random value (based on the clock)
rand('state',sum(100*clock));
% WaitSecs(.5)
screenRect=get(0,'ScreenSize');
reps=100; % how many random shuffles do you want to do?
%%%%%%%%%%%
% homedir='/Volumes/DONDERS22/SPATMASSMEMANALYZE'
% cd '/Users/jeremywolfe/Documents/MATLAB2016/SPATMASSMEMANALYZE'
% cd='/Volumes/DONDERS22/SPATMASSMEMANALYZE'
% CLAIRE: YOU READ IN YOUR EXCEL FILE DATA HERE
SMMTMM=csvread('csv2/FullInstruction.csv');
SMMTMM(1:2,:)
save SMMTMM
load SMMTMM
load SingleStreamAnalyzeOut
SMMTMM(1:2,:)
[nlines zz]=size(SMMTMM)
blockstring=string(SMMTMM); % convert that column to a string
TestTrials=find(strcmp(SMMTMM.blockName,'Spatial')); % all the test lines

OldNewCorrectLines=find(SMMTMM.isCorrect==1); % should be all the hits on the old new test
OldNewErrorLines=find(SMMTMM.isCorrect==0); % should be all the errors on the old new test
NewItemLines=find(SMMTMM.isOldItem==0); % all the first appearances of items regardless of errors, etc
OldItemLines=find(SMMTMM.isOldItem==1); % all the second appearances of items regardless of errors, etc
Item2Lines=intersect(OldItemLines,OldNewCorrectLines); % eliminate errors, so these are HIT lines
Item2Lines=intersect(Item2Lines,TestTrials); % eliminate practice
Item1Lines=Item2Lines-SMMTMM.item_lag(Item2Lines); % Should be all the correct first items lines paired with correct Item2Lines lines
Item1FALines=intersect(NewItemLines,OldNewErrorLines); % these are FA lines

% This is the basic old/new analysis
for ThisObs=1:max(SMMTMM.obsOrder) % go through every observer
    ObsLines=find(SMMTMM.obsOrder==ThisObs);
    ObsN=length(ObsLines);
    ObsOld=intersect(OldItemLines,ObsLines); % Old Items for this Obs
    ObsNew=intersect(NewItemLines,ObsLines); % New Items for this Obs
    ObsHit=intersect(Item2Lines,ObsLines); % hits for this Obs
    ObsFA=intersect(Item1FALines,ObsLines); % FA for this Obs
    phit=length(ObsHit)/length(ObsOld);
    pfa=length(ObsFA)/length(ObsNew);
    zhit=norminv(phit);
    zfa=norminv(pfa);
    dprime=zhit-zfa;
    crit=(zhit+zfa)/-2;
    CountSummary(ThisObs,:)=[ThisObs max(SMMTMM.Subject(ObsLines)) (ObsN) ...
        round(100*phit) round(100*pfa) zhit zfa dprime crit];
    % ObsCOunt ObsNum TotalTrials phit pfa zhit zfa dprime crit
end
'ObsCOunt ObsNum TotalTrials phit pfa'
CountSummary
csvwrite(['CountSummarySMMTMM.csv'],CountSummary)

% Let's do errors in terms of distances in cells not pixels

n=length(Item2Lines); % just a count
reps=1000; % for the simulation part
SingleStreamAnalyzeOut=zeros(1,24);
% 1 - i
% 2 - obs
% 3 - obsN
% 4 -lineItem1,
% 5-lineItem2,
% 6-lag,
% 7-log2(lag)bin,
% 8- x1,
% 9- y1,
% 10- ClickX(cell)
% 11- ClickY(cell)
% 12 - Error Distance(cell)
% 13 -simulatedError
% 14 -simulatedErrorSD
% 15 - T error
% 16 - abs(T error)
% 17 - Simulated T
% 18 - Simulated T error
% 19 - SD Simulated T
% 20 - SD Simulated T error
% 21 - P(SimSpatError < ROI)
% 22 - simerror1(1)
% 23 - simtimeerror1(1)
% 24 - simtimeerror2(1)

% Also create ROI simulation data file
ROI_Trialdata=zeros(n,57);
% 1 - i
% 2 - obs
% 3 - obsN
% 4-lag,
% 5-log2(lag)bin
% 6-18 = ROI flag (0,1)
% 19-31 = sROI 0:0.5:6
% 32-44 = tempROI flag (0,1)
% 45-57 = ptempSimROI

% creat the Log2Bins ... actually, that is in the dataset already
LogBin=zeros(length(SMMTMM.item_lag),1);
a=find(SMMTMM.item_lag > 0);
LogBin(a)=round(log2(SMMTMM.item_lag(a)));

d=[];
SpatROI=1.5;
figflag=2;
ReCalcFlag=1;
if ReCalcFlag > 0
    for i=1:n % for each HIT trial
        x1=SMMTMM.oldLoc_col(Item2Lines(i)); % xloc of the original item (col = X)
        y1=SMMTMM.oldLoc_row(Item2Lines(i)); % yloc of the original item (row = Y)
        x2=SMMTMM.clickLoc_col(Item2Lines(i)); % xloc of the original item (col = X)
        y2=SMMTMM.clickLoc_row(Item2Lines(i)); % yloc of the original item (row = Y)
        cellError(i)=sqrt(((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2))); % this is the error in cell units
        timeError(i)=SMMTMM.timeBarErr_RespMinusOld(Item2Lines(i));
        o=find(SMMTMM.obsOrder==SMMTMM.obsOrder(Item2Lines(i))); % the lines for the current observer
        olines=intersect(Item2Lines,o);
        nolines=length(olines);
        simerror=[];
        simtimeerror1=[];
        simtimeerror2=[];
        nowt=SMMTMM.timeBar_now(Item2Lines(i)); % This is just a short version of now
        for r=1:reps
            z=randi(nolines);
            sx2=SMMTMM.clickLoc_col(olines(z)); % a random x click from that obse
            sy2=SMMTMM.clickLoc_row(olines(z)); % a paired random y click from that obs
            simerror(r)=sqrt(((x1-sx2)*(x1-sx2))+((y1-sy2)*(y1-sy2)));
            simtimeerror1(r)=randi(ceil(nowt))-SMMTMM.timeBar_old(Item2Lines(i)); % pick a random number between zero and current time
            simtimeerror2(r)=((randn()*(nowt)*0.1)+(nowt*0.75)); % pick a random number N(0.75NOW)+/-.1NOW , subtract actual first time
            simtimeerror2(r)=min(simtimeerror2(r), SMMTMM.timeBar_now(Item2Lines(i))); % no clicks in the future
            simtimeerror2(r)=max(0, SMMTMM.timeBar_now(Item2Lines(i))); % no clicks below zero
            simtimeerror2(r)=simtimeerror2(r)-SMMTMM.timeBar_old(Item2Lines(i)); % subtract actual first time
        end
        GuessError(i)=mean(simerror);
        GuessSD(i)=std(simerror);
        MeanSimTimeError1=mean(simtimeerror1);
        MeanSimAbsTimeError1=mean(abs(simtimeerror1));
        SDSimTimeError1=std(simtimeerror1);
        SDSimAbsTimeError1=std(abs(simtimeerror1));
        pSimSpatInROI=sum(simerror<SpatROI)/reps;

        % here is the main output of the guess simulation
        SingleStreamAnalyzeOut(i,:)=[i SMMTMM.Subject(Item2Lines(i)) SMMTMM.obsOrder(Item2Lines(i))...
            Item1Lines(i) Item2Lines(i) Item2Lines(i)-Item1Lines(i) LogBin(Item2Lines(i))...
            x1 y1 x2 y2 cellError(i) GuessError(i) GuessSD(i) ...
            timeError(i) abs(timeError(i)) MeanSimTimeError1 MeanSimAbsTimeError1 SDSimTimeError1 SDSimTimeError1 pSimSpatInROI,...
            simerror(1) simtimeerror1(1) simtimeerror2(1)];
        % do the ROI calc
        % Simulation is pct of clicks falling in ROI
        % Real data is a 0,1 flag for that trial
        k=0;
        psROI=zeros(1,13);
        for ROI=0:0.5:6
            k=k+1;
            psROI(k)=sum(simerror<=ROI)/reps; % pct of the simulated errors that fall into the ROI
            ROIflag(k)=(cellError(i)<=ROI); % for this trial and this ROI 1 inside, 0 outside
        end
        % temporal ROIs
        k=0;
        ptROI=zeros(1,13);
        for ROI=0:100/12:100
            k=k+1;
            ptempSimROI(k)=sum(abs(simtimeerror2)<=ROI)/reps; % pct of the simulated temporal errors that fall into the ROI (wanyi method)
            tempROIflag(k)=(abs(timeError(i))<=ROI); % for this trial and this ROI 1 inside, 0 outside
        end
        ROI_Trialdata(i,:)=[i SMMTMM.Subject(Item2Lines(i)) SMMTMM.obsOrder(Item2Lines(i))...
            Item2Lines(i)-Item1Lines(i) LogBin(Item2Lines(i))...
            ROIflag psROI tempROIflag ptempSimROI];
        if mod(i,400)==1 % just for check up
            [i tempROIflag]
        end

    end
    csvwrite(['SingleStreamAnalyzeOutSMMTMM.csv'],SingleStreamAnalyzeOut)
    % SingleStreamAnalyzeOut
    save SingleStreamAnalyzeOut

    csvwrite(['ROI_Trialdata.csv'],ROI_Trialdata)
    % SingleStreamAnalyzeOut
    save ROI_Trialdata
end


ROIs=0:0.5:6; % the values of the ROI
tempROI=0:100/12:100; % the values of the time ROI
ROIoutput=zeros(13,23);
ROIoutput(:,1)=ROIs;
simROIoutput=zeros(13,23);
simROIoutput(:,1)=ROIs;
difROIoutput=zeros(13,23);
difROIoutput(:,1)=ROIs;
% The temporal ROI functions
timeROIoutput=zeros(13,23);
timeROIoutput(:,1)=tempROI;
timesimROIoutput=zeros(13,23);
timesimROIoutput(:,1)=tempROI;
timedifROIoutput=zeros(13,23);
timedifROIoutput(:,1)=tempROI;


for ThisObs=1:max(ROI_Trialdata(:,2)) % go through every observer
    ObsLines=find(ROI_Trialdata(:,2)==ThisObs);
    % skip the lag for now
    %     for loglagbin=1:7
    %         LagLines=SimROIdata(:,5)==loglagbin; % get that lag
    %         OLagLines=intersect(ObsLines, LagLines)
    for ROIindex=1:13
        p(ROIindex)=sum(ROI_Trialdata(ObsLines,5+ROIindex))/length(ObsLines); % should be the percentage in that ROI for that Obs
        s(ROIindex)=mean(ROI_Trialdata(ObsLines,18+ROIindex)); % % should be the simulated percentage in that ROI for that Obs
        t(ROIindex)=sum(ROI_Trialdata(ObsLines,31+ROIindex))/length(ObsLines); % should be the percentage in that temporal ROI for that Obs
        ts(ROIindex)=mean(ROI_Trialdata(ObsLines,44+ROIindex)); % % should be the simulated percentage in that temporal ROI for that Obs
    end
    d=p-s;
    td=t-ts;
    ROIoutput(:,ThisObs+1)=p;
    simROIoutput(:,ThisObs+1)=s;
    difROIoutput(:,ThisObs+1)=d;
    timeROIoutput(:,ThisObs+1)=t;
    timesimROIoutput(:,ThisObs+1)=ts;
    timedifROIoutput(:,ThisObs+1)=td;
    if figflag == 1
        figure(30+ThisObs)
        if ThisObs < 7
            set(30+ThisObs,'position',[(ThisObs-1)*300 0 300 300]);
        elseif ThisObs < 13
            set(30+ThisObs,'position',[(ThisObs-7)*300 300 300 300]);
        elseif ThisObs < 19
            set(30+ThisObs,'position',[(ThisObs-13)*300 600 300 300]);
        else
            set(30+ThisObs,'position',[(ThisObs-19)*300 900 300 300]);
        end
        set(30+ThisObs,'name',['Space vs Time']);
        title(['Space vs Time Obs', num2str(ThisObs)],'Color',[0 .5 .7],'FontSize',18);
        xlabel('Space','Color',[0 0 0],'FontSize',18);
        ylabel('Time','Color',[0 0 0],'FontSize',18);
        axis([0 10 -100 100]);
        drawnow
        hold on
        c=hsv2rgb([rand(),.6,.8]);
        scatter(cellError(ObsLines), timeError(ObsLines),36,c,'filled')
        drawnow
        hold on
    end
    if figflag == 2
        figure(30+ThisObs)
        if ThisObs < 7
            set(30+ThisObs,'position',[(ThisObs-1)*300 0 300 300]);
        elseif ThisObs < 13
            set(30+ThisObs,'position',[(ThisObs-7)*300 300 300 300]);
        elseif ThisObs < 19
            set(30+ThisObs,'position',[(ThisObs-13)*300 600 300 300]);
        else
            set(30+ThisObs,'position',[(ThisObs-19)*300 900 300 300]);
        end
        set(30+ThisObs,'name',['Space vs Time']);
        title(['Space vs Time Obs', num2str(ThisObs)],'Color',[0 .5 .7],'FontSize',18);
        xlabel('Space','Color',[0 0 0],'FontSize',18);
        ylabel('Time','Color',[0 0 0],'FontSize',18);
        axis([0 1 0 1]);
        drawnow
        hold on
        c=hsv2rgb([rand(),.4,1]);
        plot(ROIoutput(:,ThisObs+1), timeROIoutput(:,ThisObs+1),'-ks','LineWidth',2,...
            'MarkerEdgeColor','k',...
            'MarkerFaceColor',c,...
            'MarkerSize',8)
        drawnow
        hold on
        plot(simROIoutput(:,ThisObs+1), timesimROIoutput(:,ThisObs+1),'--rs','LineWidth',2)
        drawnow
        hold on
    end
end
% plot all the data
ThisObs=24;
figure(30+ThisObs)
set(30+ThisObs,'position',[(ThisObs-19)*300 900 300 300]);
set(30+ThisObs,'name',['Space vs Time']);
title(['Space vs Time Obs - ALL DATA'],'Color',[0 .5 .7],'FontSize',18);
xlabel('Space','Color',[0 0 0],'FontSize',18);
ylabel('Time','Color',[0 0 0],'FontSize',18);
axis([0 10 -100 100]);
drawnow
hold on
c=hsv2rgb([rand(),.6,0]);
scatter(cellError, timeError,16,c,'filled')
drawnow
hold on

csvwrite(['SMMTMM_ROIoutput.csv'],ROIoutput)
csvwrite(['SMMTMM_difROIoutput.csv'],difROIoutput)
csvwrite(['SMMTMM_simROIoutput.csv'],simROIoutput)
csvwrite(['SMMTMM_TimeROIoutput.csv'],timeROIoutput)
csvwrite(['SMMTMM_TimedifROIoutput.csv'],timedifROIoutput)
csvwrite(['SMMTMM_TimesimROIoutput.csv'],timesimROIoutput)
