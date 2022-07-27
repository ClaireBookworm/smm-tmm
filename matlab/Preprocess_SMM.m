previousOs = 0;
files = dir('*.txt') ;   % you are in the folder of files 
N = length(files) ;
% loop for each file 

comments = {};

for i = 1:N
    thisfileName = files(i).name ;
    fileName = thisfileName(1:end-4);
    fileID = fopen(thisfileName);
    formatSpec = '%s';
    C_text = textscan(fileID,formatSpec,'Delimiter','\t');
    
    A = C_text{1,1}{1,1};
    % clean up the extra symbols 
    A2 = strfind(A, '"'); 
    A(A2) = [];
    % for 2018 and after 
    %A3 = split(A,['{']); % the actual trial data are stored in {}, an  
    % easy way to separate the trial data is to split the line at every '{'
    % for 2016 and earlier
    A3 = regexp(A,'{','split')
    A3 = A3';
    
    
    subjName = i+previousOs; % increment from the previous batch 
    Subject = nan; 
    
    blockName = {};
    Setsize = nan; 
    cueLength = nan; 
    itemCount = nan;
    isOldItem = nan;
    OldItemCumCount = nan; 
    Response = {};
    isCorrect = nan;
    item_lag = nan;
    item_log2Lag = nan; 
    %thisImgLoc_ind = nan;
    thisImgLoc_x = nan;
    thisImgLoc_y = nan; 
    thisImgLoc_row = nan;
    thisImgLoc_col = nan; 
    %oldLoc_ind = nan; 
    oldLoc_x = nan;
    oldLoc_y = nan;
    oldLoc_row = nan;
    oldLoc_col = nan; 
    clickLoc_x = nan;
    clickLoc_y = nan; 
    clickLoc_row = nan;
    clickLoc_col = nan; 
    EucliDist = nan;
    timeBar_old = nan;
    timeBar_now = nan;
    timeBar_resp = nan;
    timeBarErr_RespMinusOld = nan;
    RT = nan;
    LapseTimeSinceExpStart = nan;
    imageID = nan;
    OsID = {};
    
    
   T = array2table(nan(0,17));
    counter = 0; 

     for i_line = 2:size(A3,1)-1 %first and last line are irrelevant info
        counter = counter + 1;
        
        B = A3{i_line,1}; 
        % clean up
        B2 = strfind(B, ['"']);
        B(B2) = [];
        B4 = strfind(B,'}');
        B(B4) = [];
        %B3 = split(B,[',', ':']);
        B3 = regexp(B,'[:,]','split')
        B3 = B3';
       
        Subject(counter,1) = subjName; 
        
        blockName{counter,1} = B3{2,1};%
        Setsize(counter,1) = str2double(B3{4,1}); 
        cueLength(counter,1) = str2double(B3{6,1}); 
        itemCount(counter,1) = str2double(B3{8,1}); 
        isOldItem(counter,1) = str2double(B3{12,1}); 
        OldItemCumCount(counter,1) = str2double(B3{10,1}); 
        Response{counter,1} = B3{14,1};
        isCorrect(counter,1) = str2double(B3{16,1}); 
        item_lag(counter,1) = str2double(B3{18,1}); 
        
        if item_lag(counter,1)>0
            item_log2Lag(counter,1) = round(log2(item_lag(counter,1)));
        else item_log2Lag(counter,1) = nan;
        end
       
        thisImgLoc_x(counter,1) = str2double(B3{22,1}); 
        thisImgLoc_y(counter,1) = str2double(B3{24,1}); 
        thisImgLoc_row(counter,1) = str2double(B3{26,1}); 
        thisImgLoc_col(counter,1) = str2double(B3{28,1}); 
        
        oldLoc_x(counter,1) = str2double(B3{32,1}); 
        oldLoc_y(counter,1) = str2double(B3{34,1}); 
        oldLoc_row(counter,1) = str2double(B3{36,1}); 
        oldLoc_col(counter,1) = str2double(B3{38,1}); 
        
        clickLoc_x(counter,1) = str2double(B3{40,1}); 
        clickLoc_y(counter,1) = str2double(B3{42,1}); 
        clickLoc_row(counter,1) = str2double(B3{46,1}); 
        clickLoc_col(counter,1) = str2double(B3{48,1}); 
        EucliDist(counter,1) = str2double(B3{44,1}); 
        
        timeBar_old(counter,1) = round(str2double(B3{50,1}),3); 
        timeBar_now(counter,1) = round(str2double(B3{52,1}),3); 
        timeBar_resp(counter,1) = round(str2double(B3{54,1}),3); 
        timeBarErr_RespMinusOld (counter,1) = round(str2double(B3{56,1}),3); 
        
        RT(counter,1) = str2double(B3{58,1}); 
        LapseTimeSinceExpStart(counter,1) = str2double(B3{60,1}); 
        imageID(counter,1) = str2double(B3{62,1}); 
        OsID{counter,1} = fileName;
        
     end
     
     for i_line = size(A3,1)
         
         B = A3{i_line,1}; 
        % clean up
        B2 = strfind(B, ['"']);
        B(B2) = [];
        B4 = strfind(B,'}');
        B(B4) = [];
        %B3 = split(B,[',', ':']);
        B3 = regexp(B,'[:]','split')
        B3 = B3';
         
        comments{i,1} = B3{17,1};
        
     end
     
       %save value into one table
T = table(Subject,blockName, Setsize,cueLength, itemCount,isOldItem,OldItemCumCount,Response,isCorrect,item_lag,item_log2Lag,...
    thisImgLoc_x,thisImgLoc_y,thisImgLoc_row,thisImgLoc_col,oldLoc_x,oldLoc_y,oldLoc_row,oldLoc_col,clickLoc_x,clickLoc_y ,...
    clickLoc_row,clickLoc_col,EucliDist,timeBar_old,timeBar_now, timeBar_resp,timeBarErr_RespMinusOld,...
    RT,LapseTimeSinceExpStart,imageID,OsID);

%resort the rows if anything weird happened.. 
T0 = sortrows(T,'itemCount');
T1 = sortrows(T0,'blockName');


writetable(T1, ['SMM_TMM_' num2str(subjName) '.txt']);

end

T_comment = table(comments)
writetable(T_comment, ['SMM_TMM_comment.txt']);
