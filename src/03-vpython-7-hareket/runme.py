from visual import display, color, scene
from El import *

scene = display( title='Bilek Ac/Kapa', background=(1,1,0))
scene.height = scene.width = 300
scene.center = (-2,0,0)

elim = El(scene=scene, name="El", hiz=5)

elim.setPosition((0, 0, 0))

while 1:
    if scene.kb.keys: # is there an event waiting to be processed?
        tus = scene.kb.getkey() # obtain keyboard information

        if not len(tus): continue

        if  tus == '0':     elim.serbest()
        if  tus == '1':     elim.ac()
        if  tus == '2':     elim.kapa()
        if  tus == '3':     elim.yukari()
        if  tus == '4':     elim.asagi()
        if  tus == '5':     elim.sola()
        if  tus == '6':     elim.saga()

