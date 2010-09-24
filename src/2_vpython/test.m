clc;

% sz = length(sur);
for i = 1:10
    fid = fopen('test.txt', 'a');
    tmp = randperm(4);
    tmp = tmp(1);
%     tmp = sur(i);
    fprintf(fid, '%d\n', tmp);
    fclose(fid);
    fprintf('%s : %d\n', datestr(now, 'MM:SS:FFF'), tmp);
    pause(0.2)
end
