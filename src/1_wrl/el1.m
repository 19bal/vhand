world = vrworld('hand.wrl');
open(world);
fig = view(world, '-internal');
vrdrawnow;
get(world)
fing1 = vrnode(world, 'finger1')
fields(fing1)

fing2 = vrnode(world, 'finger2')
z1 = 0:12;
x1 = 3 + zeros(size(z1));
y1 = 0.25 + zeros(size(z1));

z2 = 12:26;
x2 = 3:1.4285:23;
y2 = 0.25 + zeros(size(z2));

x3 = 23:43;
z3 = 26 + zeros(size(x3));
y3 = 0.25 + zeros(size(z3));

for i=1:length(x1)   
    fing1.translation = [x1(i) y1(i) z1(i)];
    vrdrawnow;
    pause(0.1);
end

for i=1:length(x1)   
    fing2.translation = [x1(i) y1(i) z1(i)];
    vrdrawnow;
    pause(0.1);
end