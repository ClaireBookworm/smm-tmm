% clear memory, screen and avoid blank lines
clear all, clc, format compact 


% change wd to directory of file
%%cd '/Users/luwanyi/Dropbox (Partners HealthCare)/Work from home/WolfeLab Experiments/Levari_mTurk/DataPreprocess/Os_data';

%load the txt files
files=dir('*.txt'); 

%create name of new merged txt file
fileout='SMMTMM_23Os.txt';

fout=fopen(fileout,'w');


for cntfiles=1:length(files) %has for loop go through all the .txt files 
    
  fin=fopen(files(cntfiles).name); %opens the files and creates it as a variable 
  
  while ~feof(fin) %runs while loop for file that is open
      
    fprintf(fout,'%s %d\n',fgetl(fin),cntfiles); %prins the information
    
  end
  
  fclose(fin); %closes the file
  
end

fclose(fout); %closes the merged file

clc %clears everything 