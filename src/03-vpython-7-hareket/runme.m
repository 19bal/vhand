clc;

% sz = length(sur);
for i = 1:20
    fid = fopen('test.txt', 'a');
    tmp = 6+randperm(2);
    tmp = tmp(1);
%     tmp = sur(i);
    fprintf(fid, '%d\n', tmp);
    fclose(fid);
    fprintf('%s : %d\n', datestr(now, 'MM:SS:FFF'), tmp);
    pause(0.2)
end
