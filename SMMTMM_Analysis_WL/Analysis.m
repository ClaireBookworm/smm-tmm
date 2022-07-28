% cd '/Users/wanyilyu/Dropbox (Partners HealthCare)/Current Work Space/SMM/SMM_TMM/Analysis'
%
% clear all
files = dir('*.xlsx');
thisData = csvread(files.name);
thisData = csvread('SMMTMM_23Os_withScreenSize.xlsx');
% GoodOs = [5:7, 9:16, 19:23];
%%
% scatter plot temporal response as a function of old time
% figure
% hold on
% plot([1:100],[1:100])
%  xlim([0,100])
%     ylim([0,100])
%
% for Os = 1:max(thisData.Subject)
%     Oslines = find(thisData.Subject == Os);
%     OsData = thisData(Oslines,:);
%
%     Testlines = find(strcmp(OsData.blockName,'Test'));
%     TestData = OsData(Testlines,:);
%
%     SaidOldLines = find(strcmp(TestData.Response,'SaidOld'));
%     SaidOldData = TestData(SaidOldLines,:);
%
%     scatter( SaidOldData.timeBar_old,SaidOldData.timeBar_resp)
%     %scatter( SaidOldData.timeBar_resp, repmat(2,length(SaidOldData.timeBar_resp),1))
%
% end
% ylabel('Time Click','FontSize',18)
% xlabel('Old Item Time','FontSize',18)
% %legend('optimal response' ,'Os1 ', 'Os2','FontSize',15,'Location','southeast' )

%% Individual temporal response
% for Os = 1%:max(thisData.Subject)
%
%     figure
%     hold on
%     ylabel('Time Click','FontSize',15)
%     xlabel('Old item Time','FontSize',15)
%     title(['temporal response x old item time Os ', num2str(Os)],'FontSize',18)
%
%     plot([1:100],[1:100])
%
%
%     Oslines = find(thisData.Subject == Os);
%     OsData = thisData(Oslines,:);
%
%     Testlines = find(strcmp(OsData.blockName,'Test'));
%     TestData = OsData(Testlines,:);
%
%     SaidOldLines = find(strcmp(TestData.Response,'SaidOld'));
%     SaidOldData = TestData(SaidOldLines,:);
%
%     scatter( SaidOldData.timeBar_old,SaidOldData.timeBar_resp)
%     %scatter( SaidOldData.timeBar_resp, repmat(2,length(SaidOldData.timeBar_resp),1))
%
% end


%% clicked spatial location
%
% figure
% hold on
% for Os = 3:max(thisData.Subject)
%
%     xlim([0,100])
%     ylim([0,100])
%     Oslines = find(thisData.Subject == Os);
%     OsData = thisData(Oslines,:);
%     ScreenWidth = OsData.CanvasWidth_px(1);
%
%     Testlines = find(strcmp(OsData.blockName,'Test'));
%     TestData = OsData(Testlines,:);
%
%     SaidOldLines = find(strcmp(TestData.Response,'SaidOld'));
%     PlotData = TestData(SaidOldLines,:);
%
%     clickLoc_x_scaled = PlotData.clickLoc_x/ScreenWidth*100;
%     clickLoc_y_scaled =  PlotData.clickLoc_y/ScreenWidth*100;
%
%     scatter(clickLoc_x_scaled,clickLoc_y_scaled)
%
%  end
% title('Click Locations (Os 3-23)','FontSize',15)
% ylabel('Scaled Y Axis','FontSize',15)
% xlabel('Scaled X Axis','FontSize',15)

%% temporal error by lag
% for Os = GoodOs
%
%     figure
%     hold on
%     xlabel('Lag','FontSize',15)
%     ylabel('Abs Temporal Error','FontSize',15)
%     title(['Lag x Abs Temporal Error, Os ', num2str(Os)],'FontSize',18)
%
%     Oslines = find(thisData.Subject == Os);
%     OsData = thisData(Oslines,:);
%     ScreenWidth = OsData.CanvasWidth_px(1);
%
%     Testlines = find(strcmp(OsData.blockName,'Test'));
%     TestData = OsData(Testlines,:);
%     SaidOldLines = find(strcmp(TestData.Response,'SaidOld'));
%     CorrectLines = find(TestData.isCorrect == 1);
%     FinalLines=intersect(SaidOldLines,CorrectLines);
%     PlotData = TestData(FinalLines,:);
%
%     b1 = (PlotData.item_lag)\(abs(PlotData.timeBarErr_RespMinusOld));
%     yCalc1 = b1*PlotData.item_lag;
%     plot(PlotData.item_lag,yCalc1)
%
%     scatter(PlotData.item_lag,abs(PlotData.timeBarErr_RespMinusOld))
%
% end
%
% %% estimate the distance between two item r1c1 + r2c1
%
% AllDistance = zeros(0,23);
% for Os = 3:23
%
%     Oslines = find(thisData.Subject == Os);
%     OsData = thisData(Oslines,:);
%     ScreenWidth = OsData.CanvasWidth_px(1);
%
%
%     r1line = find(OsData.thisImgLoc_row == 1);
%     r2line = find(OsData.thisImgLoc_row == 2);
%     c1line = find(OsData.thisImgLoc_col == 1);
%     r1c1line = intersect(r1line,c1line);
%     r2c1line = intersect(r2line,c1line);
%
%     Ax = mean(OsData.thisImgLoc_x(r1c1line))/ScreenWidth*100;
%     Ay = mean(OsData.thisImgLoc_y(r1c1line))/ScreenWidth*100;
%
%     Bx = mean(OsData.thisImgLoc_x(r2c1line))/ScreenWidth*100;
%     By = mean(OsData.thisImgLoc_y(r2c1line))/ScreenWidth*100;
%
%     AllDistance(Os) = EucledianDistance(Ax,Ay, Bx,By)
%
% end

%% Histogram of temporal Error

figure
hold on
HITLines =  find(strcmp(thisData.Message,'HIT'));
histogram(thisData.timeBarErr_RespMinusOld(HITLines),100,'Normalization','probability')

title('Temporal Error Distribution','FontSize',18)
ylabel('Response Probability','FontSize',18)
xlabel('Error (ResponseTime - OldItemTime)','FontSize',18)
X = zeros(1,11);
Y = [0:10]/10;
plot(X,Y)
ylim([0,0.14])

% %Histogram of the four guessing Os
% figure
% hold on
%
% HITLines =  find(strcmp(thisData.Message,'HIT'));
% GuessOs = [4,8,17,18];
% GuessOsLines = find(thisData.Subject == GuessOs);
% GuessOsHITLines = intersect(HITLines,GuessOsLines);
%
% histogram(thisData.timeBarErr_RespMinusOld(GuessOsHITLines),100,'Normalization','probability')
%
% title('Temporal Error Distribution (Four Guess Os)','FontSize',18)
% ylabel('Response Probability','FontSize',18)
% xlabel('Error (ResponseTime - OldItemTime)','FontSize',18)
% X = zeros(1,11);
% Y = [0:10]/10;
% plot(X,Y)
% ylim([0,0.14])
% xlim([-100,100])


%% Simulate Temporal Response Guesses

SimTemporalErr = [];

GuessProportion = 0.5;

for Os = 1:23

    Oslines = find(thisData.Subject == Os);
    OsData = thisData(Oslines,:);

    Testlines = find(strcmp(OsData.blockName,'Test'));
    Oldlines = find(OsData.isOldItem ==1);
    GetLines = intersect(Oldlines,Testlines);

    AllTimePoints = OsData.timeBar_now(GetLines);
    CorrectOldTime = OsData.timeBar_old(GetLines);

    for t = 1:length(AllTimePoints)

        for iteration = 1:200

            if rand< GuessProportion

                %if people tend to guess near the current time
                MinTime = max(0, 0.75*AllTimePoints(t));
                MaxTime = AllTimePoints(t);
                %Guess #1 guess falls onto a normal distribution with mean =
                %0.7 * current time
                meanTime = min(MaxTime,MinTime);
                GuessTime = normrnd(meanTime,14);

%                 %Guess #2 random location before the current time
%                 MinTime = 0;
%                 MaxTime =  AllTimePoints(t);
%                 GuessTime = MinTime + (MaxTime-MinTime).*rand;
%
                thisError = GuessTime - CorrectOldTime(t);
                SimTemporalErr(Os,t,iteration) = thisError;

            else
                r = normrnd(-0.6,3.5) ;

                SimTemporalErr(Os,t,iteration) = r;
            end

        end

    end
end
SimTemporalErr = SimTemporalErr(:);
histogram(SimTemporalErr,100,'Normalization','probability')

%% Spatial capacity: Pct of good clicks for each ROI size

%
% % Scale the error
%
% AllROIsCorrectCount = nan(23,8);
% AllROIsCorrectPct = nan(23,8);
%
% for Os = 3: 23
%
%     Oslines = find(thisData.Subject == Os);
%     OsData = thisData(Oslines,:);
%     ScreenWidth = OsData.CanvasWidth_px(1);
%
%     HITlines = find(strcmp(OsData.Message,'HIT'));
%     Testlines = find(strcmp(OsData.blockName,'Test'));
%     GetLines = intersect(HITlines,Testlines);
%
%     GetData = OsData(GetLines,:);
%
%     for ROI = 1:14
%
%         InROIcount = 0;
%
%         for trial = 1:length(GetLines)
%
%             clickLoc_x_scaled = GetData.clickLoc_x(trial)/ScreenWidth*100/12.5;
%             clickLoc_y_scaled = GetData.clickLoc_y(trial)/ScreenWidth*100/12.5;
%             oldLoc_x_scaled = GetData.oldLoc_x(trial)/ScreenWidth*100/12.5;
%             oldLoc_y_scaled = GetData.oldLoc_y(trial)/ScreenWidth*100/12.5;
%
%             if (clickLoc_x_scaled >= (oldLoc_x_scaled-ROI/2) & clickLoc_x_scaled <= (oldLoc_x_scaled+ROI/2))
%                 if(clickLoc_y_scaled >= (oldLoc_y_scaled-ROI/2) & clickLoc_y_scaled <= (oldLoc_y_scaled+ROI/2))
%                     InROIcount = InROIcount + 1;
%                 end
%             end
%             %error_scaled = EucledianDistance( clickLoc_x_scaled,clickLoc_y_scaled,oldLoc_x_scaled,oldLoc_y_scaled )
%
%         end
%
%         AllROIsCorrectPct(Os,ROI) = InROIcount/length(GetLines);
%         AllROIsCorrectCount(Os,ROI) = InROIcount;
%
%     end
% % Calculate how many is correct
%
% end

%% Spatial capacity: Pct of Guess clicks for each ROI size

%
% GuessROIsCorrectCount = nan(23,8);
% GuessROIsCorrectPct = nan(23,8);
%
% for Os = 3: 23
%
%     Oslines = find(thisData.Subject == Os);
%     OsData = thisData(Oslines,:);
%     ScreenWidth = OsData.CanvasWidth_px(1);
%
%     HITlines = find(strcmp(OsData.Message,'HIT'));
%     Testlines = find(strcmp(OsData.blockName,'Test'));
%     GetLines = intersect(HITlines,Testlines);
%
%     GetData = OsData(GetLines,:);
%
%     for ROI = 1:14
%
%         InROIcount = 0;
%
%         for trial = 1:length(GetLines)
%
%             oldLoc_x_scaled = GetData.oldLoc_x(trial)/ScreenWidth*100/12.5;
%             oldLoc_y_scaled = GetData.oldLoc_y(trial)/ScreenWidth*100/12.5;
%
%             % Get a random click from all clicks
%
%             R = Shuffle([1:length(GetLines)]);
%             RR = R(1);
%
%             GuessclickLoc_x_scaled = GetData.clickLoc_x(RR)/ScreenWidth*100/12.5;
%             GuessclickLoc_y_scaled = GetData.clickLoc_y(RR)/ScreenWidth*100/12.5;
%
%
%             if (GuessclickLoc_x_scaled >= (oldLoc_x_scaled-ROI/2) & GuessclickLoc_x_scaled <= (oldLoc_x_scaled+ROI/2))
%                 if(GuessclickLoc_y_scaled >= (oldLoc_y_scaled-ROI/2) & GuessclickLoc_y_scaled <= (oldLoc_y_scaled+ROI/2))
%                     InROIcount = InROIcount + 1;
%                 end
%             end
%             %error_scaled = EucledianDistance( clickLoc_x_scaled,clickLoc_y_scaled,oldLoc_x_scaled,oldLoc_y_scaled )
%
%         end
%
%         GuessROIsCorrectPct(Os,ROI) = InROIcount/length(GetLines);
%         GuessROIsCorrectCount(Os,ROI) = InROIcount;
%
%     end
% % Calculate how many is correct
%
% end
%
%% Temporol Capacity: Pct of good clicks for each ROI size
% test different ranges of time
%
% TempROIsCorrectCount = nan(23,50);
% TempROIsCorrectPct = nan(23,50);
%
%
% for Os = 1: 23
%
%     Oslines = find(thisData.Subject == Os);
%     OsData = thisData(Oslines,:);
%     ScreenWidth = OsData.CanvasWidth_px(1);
%
%     HITlines = find(strcmp(OsData.Message,'HIT'));
%     Testlines = find(strcmp(OsData.blockName,'Test'));
%     GetLines = intersect(HITlines,Testlines);
%
%     GetData = OsData(GetLines,:);
%
%     for ROI = 1: 100
%         InROIcount = 0;
%
%         for trial = 1: length(GetLines)
%
%             timebarOld = GetData.timeBar_old(trial);
%             timebarResp = GetData.timeBar_resp(trial);
%
%             if abs(timebarOld-timebarResp)<= (ROI-1+0.01)/2
%                 InROIcount = InROIcount+1;
%             end
%         end
%
%         TempROIsCorrectCount(Os,ROI) = InROIcount;
%         TempROIsCorrectPct(Os,ROI) = InROIcount/length(GetLines);
%     end
% end

% Temporol Capacity: Pct of good clicks for each ROI size
%test different ranges of time

Guess2TempROIsCorrectCount = nan(23,50);
Guess2TempROIsCorrectPct = nan(23,50);


for Os = 1: 23

    Oslines = find(thisData.Subject == Os);
    OsData = thisData(Oslines,:);
    ScreenWidth = OsData.CanvasWidth_px(1);

    HITlines = find(strcmp(OsData.Message,'HIT'));
    Testlines = find(strcmp(OsData.blockName,'Test'));
    GetLines = intersect(HITlines,Testlines);

    GetData = OsData(GetLines,:);

    for ROI = 1: 100
        InROIcount = 0;

        for trial = 1: length(GetLines)

            timebarOld = GetData.timeBar_old(trial);
            timebarNow = GetData.timeBar_now(trial);

            %timebarResp = GetData.timeBar_resp(trial);

            %Guess 1
            RR = 0 + (timebarNow-0).*rand;

            %Guess #2 guess falls onto a normal distribution with mean =
            %0.7 * current time
            %if people tend to guess near the current time
            MinTime = max(0, 0.75*timebarNow);
            MaxTime = timebarNow;
            meanTime = min(MaxTime,MinTime);
            RR = normrnd(meanTime,14);

            if abs(timebarOld-RR)<= (ROI-1+0.01)/2
                InROIcount = InROIcount+1;
            end
        end

        Guess2TempROIsCorrectCount(Os,ROI) = InROIcount;
        Guess2TempROIsCorrectPct(Os,ROI) = InROIcount/length(GetLines);
    end
end

