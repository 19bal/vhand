clear all;  close all;  clc;

dbg = true;

fnm_alpha = pathos('_bkp/renkli_marker_alpha.csv');
if ~exist(fnm_alpha),
    error(sprintf('19bal/heg/.../05-vid-renkli-marker/_bkp/%s yi buraya kopyala\nVEYA bunu dene: https://github.com/downloads/19bal/heg/renkli_marker_alpha.csv', fnm_alpha));  
end

disp('anlik.py betigi calisyor degil mi');

alpha = csvread(fnm_alpha);

% preprocess
% a) NaN
idx = find(isnan(alpha));
alpha(idx) = alpha(idx-1);

% b) 0
idx = find(alpha==0);
alpha(idx) = alpha(idx-1);

alpha = alpha - mean(alpha);
alpha = round(alpha);

if dbg, plot(alpha),    end

% ilkleme
fid = fopen('test.txt', 'a');
tmp = round(1.5 * alpha(1));
fprintf(fid, '%d\n', tmp);
fclose(fid);
pause(2)

for i = 1:5:length(alpha)
    fid = fopen('test.txt', 'a');

    tmp = round(1.5 * alpha(i));

    fprintf(fid, '%d\n', tmp);
    fclose(fid);
    
    fprintf('%s : %d\n', datestr(now, 'MM:SS:FFF'), tmp);
    pause(0.2)
end

