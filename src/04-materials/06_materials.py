from visual import *
grid = ( (color.red, (1, 0.7 ,0)),
         ((0, 1, 0.3), color.magenta) )
tgrid = materials.texture(data=grid,
                          mapping="sign",
                          interpolate=False)
box(axis=(0,0,1), material=tgrid)
