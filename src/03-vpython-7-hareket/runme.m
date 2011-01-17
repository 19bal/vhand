clc;

anlik = [1:5:75 70:-10:-70 -60:20:90];

nums = anlik;

for i = 1:length(nums)
    fid = fopen('test.txt', 'a');
    %tmp = 6+randperm(2);
    %tmp = tmp(1);
    tmp = nums(i);

    fprintf(fid, '%d\n', tmp);
    fclose(fid);
    fprintf('%s : %d\n', datestr(now, 'MM:SS:FFF'), tmp);
    pause(0.3)
end
