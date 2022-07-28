# Generated with SMOP  0.41
import math
from operator import length_hint
import string
import numpy
from scipy import rand
# from numpy import numpy.arange
from smop.libsmop import *
# SingleStreamSMMTMMAnalyze8.m

# v6 cleans up the names of the simulated time error and computes it two
# different ways.
# also we output single simulated values for each trial so we can look at
# predicted correlations

# clear everything before you begin
# clear('all')
# close_('all')
# set the state of the random number generator to some random value (based on the clock)
rand('state', sum(dot(100, clock)))
# WaitSecs(.5)
screenRect = get(0, 'ScreenSize')
# SingleStreamSMMTMMAnalyze8.m:12
reps = 100
# SingleStreamSMMTMMAnalyze8.m:13

###########
# homedir='/Volumes/DONDERS22/SPATMASSMEMANALYZE'
# cd '/Users/jeremywolfe/Documents/MATLAB2016/SPATMASSMEMANALYZE'
# cd='/Volumes/DONDERS22/SPATMASSMEMANALYZE'
# CLAIRE: YOU READ IN YOUR EXCEL FILE DATA HERE
SMMTMM = readtable('csv2/FullInstruction.csv')
# SingleStreamSMMTMMAnalyze8.m:19
SMMTMM(numpy.arange(1, 2), numpy.arange())
# save('SMMTMM')
load('SMMTMM')
load('SingleStreamAnalyzeOut')
SMMTMM(numpy.arange(1, 2), numpy.arange())
nlines, zz = size(SMMTMM, nargout=2)
# SingleStreamSMMTMMAnalyze8.m:25
blockstring = string(SMMTMM)
# SingleStreamSMMTMMAnalyze8.m:26

TestTrials = find(strcmp(SMMTMM.blockName, 'Spatial'))
# SingleStreamSMMTMMAnalyze8.m:27

OldNewCorrectLines = find(SMMTMM.isCorrect == 1)
# SingleStreamSMMTMMAnalyze8.m:29

OldNewErrorLines = find(SMMTMM.isCorrect == 0)
# SingleStreamSMMTMMAnalyze8.m:30

NewItemLines = find(SMMTMM.isOldItem == 0)
# SingleStreamSMMTMMAnalyze8.m:31

OldItemLines = find(SMMTMM.isOldItem == 1)
# SingleStreamSMMTMMAnalyze8.m:32

Item2Lines = numpy.intersect1d(OldItemLines, OldNewCorrectLines)
# SingleStreamSMMTMMAnalyze8.m:33

Item2Lines = numpy.intersect1d(Item2Lines, TestTrials)
# SingleStreamSMMTMMAnalyze8.m:34

Item1Lines = Item2Lines - SMMTMM.item_lag(Item2Lines)
# SingleStreamSMMTMMAnalyze8.m:35

Item1FALines = numpy.intersect1d(NewItemLines, OldNewErrorLines)
# SingleStreamSMMTMMAnalyze8.m:36

# This is the basic old/new analysis
for ThisObs in numpy.arange(1, max(SMMTMM.obsOrder)).reshape(-1):
    ObsLines = find(SMMTMM.obsOrder == ThisObs)
# SingleStreamSMMTMMAnalyze8.m:40
    ObsN = length_hint(ObsLines)
# SingleStreamSMMTMMAnalyze8.m:41
    ObsOld = numpy.intersect1d(OldItemLines, ObsLines)
# SingleStreamSMMTMMAnalyze8.m:42
    ObsNew = numpy.intersect1d(NewItemLines, ObsLines)
# SingleStreamSMMTMMAnalyze8.m:43
    ObsHit = numpy.intersect1d(Item2Lines, ObsLines)
# SingleStreamSMMTMMAnalyze8.m:44
    ObsFA = numpy.intersect1d(Item1FALines, ObsLines)
# SingleStreamSMMTMMAnalyze8.m:45
    phit = length_hint(ObsHit) / length_hint(ObsOld)
# SingleStreamSMMTMMAnalyze8.m:46
    pfa = length_hint(ObsFA) / length_hint(ObsNew)
# SingleStreamSMMTMMAnalyze8.m:47
    zhit = norminv(phit)
# SingleStreamSMMTMMAnalyze8.m:48
    zfa = norminv(pfa)
# SingleStreamSMMTMMAnalyze8.m:49
    dprime = zhit - zfa
# SingleStreamSMMTMMAnalyze8.m:50
    crit = (zhit + zfa) / - 2
# SingleStreamSMMTMMAnalyze8.m:51
    CountSummary[ThisObs, numpy.arange()] = numpy.concatenate([ThisObs, max(SMMTMM.Subject(
        ObsLines)), (ObsN), round(dot(100, phit)), round(dot(100, pfa)), zhit, zfa, dprime, crit])
# SingleStreamSMMTMMAnalyze8.m:52

    'ObsCOunt ObsNum TotalTrials phit pfa'
    CountSummary
    csvwrite(numpy.concatenate(['CountSummarySMMTMM.csv']), CountSummary)
    # Let's do errors in terms of distances in cells not pixels

    n = length_hint(Item2Lines)
# SingleStreamSMMTMMAnalyze8.m:62

    reps = 1000
# SingleStreamSMMTMMAnalyze8.m:63

    SingleStreamAnalyzeOut = zeros(1, 24)
# SingleStreamSMMTMMAnalyze8.m:64
    # 1 - i
# 2 - obs
# 3 - obsN
# 4 -lineItem1,
# 5-lineItem2,
# 6-lag,
# 7-log2(lag)bin,
# 8- x1,
# 9- y1,
# 10- ClickX(cell)
# 11- ClickY(cell)
# 12 - Error Distance(cell)
# 13 -simulatedError
# 14 -simulatedErrorSD
# 15 - T error
# 16 - abs(T error)
# 17 - Simulated T
# 18 - Simulated T error
# 19 - SD Simulated T
# 20 - SD Simulated T error
# 21 - P(SimSpatError < ROI)
# 22 - simerror1(1)
# 23 - simtimeerror1(1)
# 24 - simtimeerror2(1)

    # Also create ROI simulation data file
    ROI_Trialdata = zeros(n, 57)
# SingleStreamSMMTMMAnalyze8.m:91
    # 1 - i
# 2 - obs
# 3 - obsN
# 4-lag,
# 5-log2(lag)bin
# 6-18 = ROI flag (0,1)
# 19-31 = sROI 0:0.5:6
# 32-44 = tempROI flag (0,1)
# 45-57 = ptempSimROI

    # creat the Log2Bins ... actually, that is in the dataset already
    LogBin = zeros(length_hint(SMMTMM.item_lag), 1)
# SingleStreamSMMTMMAnalyze8.m:103
    a = find(SMMTMM.item_lag > 0)
# SingleStreamSMMTMMAnalyze8.m:104
    LogBin[a] = round(log2(SMMTMM.item_lag(a)))
# SingleStreamSMMTMMAnalyze8.m:105
    d = []
# SingleStreamSMMTMMAnalyze8.m:107
    SpatROI = 1.5
# SingleStreamSMMTMMAnalyze8.m:108
    figflag = 2
# SingleStreamSMMTMMAnalyze8.m:109
    ReCalcFlag = 1
# SingleStreamSMMTMMAnalyze8.m:110
    if ReCalcFlag > 0:
        for i in numpy.arange(1, n).reshape(-1):
            x1 = SMMTMM.oldLoc_col(Item2Lines(i))
# SingleStreamSMMTMMAnalyze8.m:113
            y1 = SMMTMM.oldLoc_row(Item2Lines(i))
# SingleStreamSMMTMMAnalyze8.m:114
            x2 = SMMTMM.clickLoc_col(Item2Lines(i))
# SingleStreamSMMTMMAnalyze8.m:115
            y2 = SMMTMM.clickLoc_row(Item2Lines(i))
# SingleStreamSMMTMMAnalyze8.m:116
            cellError[i] = sqrt((dot((x1 - x2), (x1 - x2))) +
                                (dot((y1 - y2), (y1 - y2))))
# SingleStreamSMMTMMAnalyze8.m:117
            timeError[i] = SMMTMM.timeBarErr_RespMinusOld(Item2Lines(i))
# SingleStreamSMMTMMAnalyze8.m:118
            o = find(SMMTMM.obsOrder == SMMTMM.obsOrder(Item2Lines(i)))
# SingleStreamSMMTMMAnalyze8.m:119
            olines = numpy.intersect1d(Item2Lines, o)
# SingleStreamSMMTMMAnalyze8.m:120
            nolines = length_hint(olines)
# SingleStreamSMMTMMAnalyze8.m:121
            simerror = []
# SingleStreamSMMTMMAnalyze8.m:122
            simtimeerror1 = []
# SingleStreamSMMTMMAnalyze8.m:123
            simtimeerror2 = []
# SingleStreamSMMTMMAnalyze8.m:124
            nowt = SMMTMM.timeBar_now(Item2Lines(i))
# SingleStreamSMMTMMAnalyze8.m:125
            for r in numpy.arange(1, reps).reshape(-1):
                z = randi(nolines)
# SingleStreamSMMTMMAnalyze8.m:127
                sx2 = SMMTMM.clickLoc_col(olines(z))
# SingleStreamSMMTMMAnalyze8.m:128
                sy2 = SMMTMM.clickLoc_row(olines(z))
# SingleStreamSMMTMMAnalyze8.m:129
                simerror[r] = sqrt(
                    (dot((x1 - sx2), (x1 - sx2))) + (dot((y1 - sy2), (y1 - sy2))))
# SingleStreamSMMTMMAnalyze8.m:130
                simtimeerror1[r] = randi(
                    ceil(nowt)) - SMMTMM.timeBar_old(Item2Lines(i))
# SingleStreamSMMTMMAnalyze8.m:131
                simtimeerror2[r] = (
                    (dot(dot(randn(), (nowt)), 0.1)) + (dot(nowt, 0.75)))
# SingleStreamSMMTMMAnalyze8.m:132
                simtimeerror2[r] = min(simtimeerror2(
                    r), SMMTMM.timeBar_now(Item2Lines(i)))
# SingleStreamSMMTMMAnalyze8.m:133
                simtimeerror2[r] = max(0, SMMTMM.timeBar_now(Item2Lines(i)))
# SingleStreamSMMTMMAnalyze8.m:134
                simtimeerror2[r] = simtimeerror2(
                    r) - SMMTMM.timeBar_old(Item2Lines(i))
# SingleStreamSMMTMMAnalyze8.m:135
            GuessError[i] = mean(simerror)
# SingleStreamSMMTMMAnalyze8.m:137
            GuessSD[i] = std(simerror)
# SingleStreamSMMTMMAnalyze8.m:138
            MeanSimTimeError1 = mean(simtimeerror1)
# SingleStreamSMMTMMAnalyze8.m:139
            MeanSimAbsTimeError1 = mean(abs(simtimeerror1))
# SingleStreamSMMTMMAnalyze8.m:140
            SDSimTimeError1 = std(simtimeerror1)
# SingleStreamSMMTMMAnalyze8.m:141
            SDSimAbsTimeError1 = std(abs(simtimeerror1))
# SingleStreamSMMTMMAnalyze8.m:142
            pSimSpatInROI = sum(simerror < SpatROI) / reps
# SingleStreamSMMTMMAnalyze8.m:143
            SingleStreamAnalyzeOut[i, numpy.arange()] = numpy.concatenate([i, SMMTMM.Subject(Item2Lines(i)), SMMTMM.obsOrder(Item2Lines(i)), Item1Lines(i), Item2Lines(i), Item2Lines(i) - Item1Lines(i), LogBin(Item2Lines(i)), x1, y1,
                                                                           x2, y2, cellError(i), GuessError(i), GuessSD(i), timeError(i), abs(timeError(i)), MeanSimTimeError1, MeanSimAbsTimeError1, SDSimTimeError1, SDSimTimeError1, pSimSpatInROI, simerror(1), simtimeerror1(1), simtimeerror2(1)])
# SingleStreamSMMTMMAnalyze8.m:146
            # Simulation is pct of clicks falling in ROI
        # Real data is a 0,1 flag for that trial
            k = 0
# SingleStreamSMMTMMAnalyze8.m:154
            psROI = zeros(1, 13)
# SingleStreamSMMTMMAnalyze8.m:155
            for ROI in numpy.arange(0, 6, 0.5).reshape(-1):
                k = k + 1
# SingleStreamSMMTMMAnalyze8.m:157
                psROI[k] = sum(simerror <= ROI) / reps
# SingleStreamSMMTMMAnalyze8.m:158
                ROIflag[k] = (cellError(i) <= ROI)
# SingleStreamSMMTMMAnalyze8.m:159
            # temporal ROIs
            k = 0
# SingleStreamSMMTMMAnalyze8.m:162
            ptROI = numpy.zeros(1, 13)
# SingleStreamSMMTMMAnalyze8.m:163
            for ROI in numpy.numpy.arange(0, 100, 100 / 12).reshape(-1):
                k = k + 1
# SingleStreamSMMTMMAnalyze8.m:165
                ptempSimROI[k] = sum(abs(simtimeerror2) <= ROI) / reps
# SingleStreamSMMTMMAnalyze8.m:166
                tempROIflag[k] = (abs(timeError(i)) <= ROI)
# SingleStreamSMMTMMAnalyze8.m:167
            ROI_Trialdata[i, numpy.arange()] = numpy.concatenate([i, SMMTMM.Subject(Item2Lines(i)), SMMTMM.obsOrder(
                Item2Lines(i)), Item2Lines(i) - Item1Lines(i), LogBin(Item2Lines(i)), ROIflag, psROI, tempROIflag, ptempSimROI])
# SingleStreamSMMTMMAnalyze8.m:169
            if mod(i, 400) == 1:
                numpy.concatenate([i, tempROIflag])
        csvwrite(numpy.concatenate(
            ['SingleStreamAnalyzeOutSMMTMM.csv']), SingleStreamAnalyzeOut)
        # SingleStreamAnalyzeOut
        save('SingleStreamAnalyzeOut')
        csvwrite(numpy.concatenate(['ROI_Trialdata.csv']), ROI_Trialdata)
        # SingleStreamAnalyzeOut
        save('ROI_Trialdata')

    ROIs = numpy.arange(0, 6, 0.5)
# SingleStreamSMMTMMAnalyze8.m:187

    tempROI = numpy.arange(0, 100, 100 / 12)
# SingleStreamSMMTMMAnalyze8.m:188

    ROIoutput = zeros(13, 23)
# SingleStreamSMMTMMAnalyze8.m:189
    ROIoutput[numpy.arange(), 1] = ROIs
# SingleStreamSMMTMMAnalyze8.m:190
    simROIoutput = zeros(13, 23)
# SingleStreamSMMTMMAnalyze8.m:191
    simROIoutput[numpy.arange(), 1] = ROIs
# SingleStreamSMMTMMAnalyze8.m:192
    difROIoutput = zeros(13, 23)
# SingleStreamSMMTMMAnalyze8.m:193
    difROIoutput[numpy.arange(), 1] = ROIs
# SingleStreamSMMTMMAnalyze8.m:194
    # The temporal ROI functions
    timeROIoutput = zeros(13, 23)
# SingleStreamSMMTMMAnalyze8.m:196
    timeROIoutput[numpy.arange(), 1] = tempROI
# SingleStreamSMMTMMAnalyze8.m:197
    timesimROIoutput = zeros(13, 23)
# SingleStreamSMMTMMAnalyze8.m:198
    timesimROIoutput[numpy.arange(), 1] = tempROI
# SingleStreamSMMTMMAnalyze8.m:199
    timedifROIoutput = zeros(13, 23)
# SingleStreamSMMTMMAnalyze8.m:200
    timedifROIoutput[numpy.arange(), 1] = tempROI
# SingleStreamSMMTMMAnalyze8.m:201
    for ThisObs in numpy.arange(1, max(ROI_Trialdata(numpy.arange(), 2))).reshape(-1):
        ObsLines = find(ROI_Trialdata(numpy.arange(), 2) == ThisObs)
# SingleStreamSMMTMMAnalyze8.m:205
        #     for loglagbin=1:7
    #         LagLines=SimROIdata(:,5)==loglagbin; # get that lag
    #         OLagLines=intersect(ObsLines, LagLines)
        for ROIindex in numpy.arange(1, 13).reshape(-1):
            p[ROIindex] = sum(ROI_Trialdata(
                ObsLines, 5 + ROIindex)) / length_hint(ObsLines)
# SingleStreamSMMTMMAnalyze8.m:211
            s[ROIindex] = mean(ROI_Trialdata(ObsLines, 18 + ROIindex))
# SingleStreamSMMTMMAnalyze8.m:212
            t[ROIindex] = sum(ROI_Trialdata(
                ObsLines, 31 + ROIindex)) / length_hint(ObsLines)
# SingleStreamSMMTMMAnalyze8.m:213
            ts[ROIindex] = mean(ROI_Trialdata(ObsLines, 44 + ROIindex))
# SingleStreamSMMTMMAnalyze8.m:214
        d = p - s
# SingleStreamSMMTMMAnalyze8.m:216
        td = t - ts
# SingleStreamSMMTMMAnalyze8.m:217
        ROIoutput[numpy.arange(), ThisObs + 1] = p
# SingleStreamSMMTMMAnalyze8.m:218
        simROIoutput[numpy.arange(), ThisObs + 1] = s
# SingleStreamSMMTMMAnalyze8.m:219
        difROIoutput[numpy.arange(), ThisObs + 1] = d
# SingleStreamSMMTMMAnalyze8.m:220
        timeROIoutput[numpy.arange(), ThisObs + 1] = t
# SingleStreamSMMTMMAnalyze8.m:221
        timesimROIoutput[numpy.arange(), ThisObs + 1] = ts
# SingleStreamSMMTMMAnalyze8.m:222
        timedifROIoutput[numpy.arange(), ThisObs + 1] = td
# SingleStreamSMMTMMAnalyze8.m:223
        if figflag == 1:
            figure(30 + ThisObs)
            if ThisObs < 7:
                set(30 + ThisObs, 'position',
                    numpy.concatenate([dot((ThisObs - 1), 300), 0, 300, 300]))
            else:
                if ThisObs < 13:
                    set(30 + ThisObs, 'position',
                        numpy.concatenate([dot((ThisObs - 7), 300), 300, 300, 300]))
                else:
                    if ThisObs < 19:
                        set(30 + ThisObs, 'position',
                            numpy.concatenate([dot((ThisObs - 13), 300), 600, 300, 300]))
                    else:
                        set(30 + ThisObs, 'position',
                            numpy.concatenate([dot((ThisObs - 19), 300), 900, 300, 300]))
            set(30 + ThisObs, 'name', numpy.concatenate(['Space vs Time']))
            title(numpy.concatenate(['Space vs Time Obs', num2str(
                ThisObs)]), 'Color', numpy.concatenate([0, 0.5, 0.7]), 'FontSize', 18)
            xlabel('Space', 'Color', numpy.concatenate(
                [0, 0, 0]), 'FontSize', 18)
            ylabel('Time', 'Color', numpy.concatenate(
                [0, 0, 0]), 'FontSize', 18)
            axis(numpy.concatenate([0, 10, - 100, 100]))
            drawnow
            hold('on')
            c = hsv2rgb(numpy.concatenate([rand(), 0.6, 0.8]))
# SingleStreamSMMTMMAnalyze8.m:242
            scatter(cellError(ObsLines), timeError(ObsLines), 36, c, 'filled')
            drawnow
            hold('on')
        if figflag == 2:
            figure(30 + ThisObs)
            if ThisObs < 7:
                set(30 + ThisObs, 'position',
                    numpy.concatenate([dot((ThisObs - 1), 300), 0, 300, 300]))
            else:
                if ThisObs < 13:
                    set(30 + ThisObs, 'position',
                        numpy.concatenate([dot((ThisObs - 7), 300), 300, 300, 300]))
                else:
                    if ThisObs < 19:
                        set(30 + ThisObs, 'position',
                            numpy.concatenate([dot((ThisObs - 13), 300), 600, 300, 300]))
                    else:
                        set(30 + ThisObs, 'position',
                            numpy.concatenate([dot((ThisObs - 19), 300), 900, 300, 300]))
            set(30 + ThisObs, 'name', numpy.concatenate(['Space vs Time']))
            title(numpy.concatenate(['Space vs Time Obs', num2str(
                ThisObs)]), 'Color', numpy.concatenate([0, 0.5, 0.7]), 'FontSize', 18)
            xlabel('Space', 'Color', numpy.concatenate(
                [0, 0, 0]), 'FontSize', 18)
            ylabel('Time', 'Color', numpy.concatenate(
                [0, 0, 0]), 'FontSize', 18)
            axis(numpy.concatenate([0, 1, 0, 1]))
            drawnow
            hold('on')
            c = hsv2rgb(numpy.concatenate([rand(), 0.4, 1]))
# SingleStreamSMMTMMAnalyze8.m:265
            plot(ROIoutput(numpy.arange(), ThisObs + 1), timeROIoutput(numpy.arange(), ThisObs + 1),
                 '-ks', 'LineWidth', 2, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', c, 'MarkerSize', 8)
            drawnow
            hold('on')
            plot(simROIoutput(numpy.arange(), ThisObs + 1),
                 timesimROIoutput(numpy.arange(), ThisObs + 1), '--rs', 'LineWidth', 2)
            drawnow
            hold('on')

    # plot all the data
    ThisObs = 24
# SingleStreamSMMTMMAnalyze8.m:278
    figure(30 + ThisObs)
    set(30 + ThisObs, 'position',
        numpy.concatenate([dot((ThisObs - 19), 300), 900, 300, 300]))
    set(30 + ThisObs, 'name', numpy.concatenate(['Space vs Time']))
    title(numpy.concatenate(['Space vs Time Obs - ALL DATA']),
          'Color', numpy.concatenate([0, 0.5, 0.7]), 'FontSize', 18)
    xlabel('Space', 'Color', numpy.concatenate([0, 0, 0]), 'FontSize', 18)
    ylabel('Time', 'Color', numpy.concatenate([0, 0, 0]), 'FontSize', 18)
    axis(numpy.concatenate([0, 10, - 100, 100]))
    drawnow
    hold('on')
    c = hsv2rgb(numpy.concatenate([rand(), 0.6, 0]))
# SingleStreamSMMTMMAnalyze8.m:288
    scatter(cellError, timeError, 16, c, 'filled')
    drawnow
    hold('on')
    csvwrite(numpy.concatenate(['SMMTMM_ROIoutput.csv']), ROIoutput)
    csvwrite(numpy.concatenate(['SMMTMM_difROIoutput.csv']), difROIoutput)
    csvwrite(numpy.concatenate(['SMMTMM_simROIoutput.csv']), simROIoutput)
    csvwrite(numpy.concatenate(['SMMTMM_TimeROIoutput.csv']), timeROIoutput)
    csvwrite(numpy.concatenate(
        ['SMMTMM_TimedifROIoutput.csv']), timedifROIoutput)
    csvwrite(numpy.concatenate(
        ['SMMTMM_TimesimROIoutput.csv']), timesimROIoutput)
