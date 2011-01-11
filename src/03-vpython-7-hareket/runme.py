from visual import display, color, scene
from El import *

scene = display( title='Bilek Ac/Kapa', background=(1,1,0))
scene.height = scene.width = 300
scene.center = (-2,0,0)

el = El(scene=scene, name="El", hiz=30)

el.setPosition((0, 0, 0))

while 1:
    if scene.kb.keys: # is there an event waiting to be processed?
        tus = scene.kb.getkey() # obtain keyboard information

        if not len(tus): continue

        if  tus == '0':     el.serbest()
        if  tus == '1':     el.ac()
        if  tus == '2':     el.kapa()
        if  tus == '3':     el.yukari()
        if  tus == '4':     el.asagi()
        if  tus == '5':     el.sola()
        if  tus == '6':     el.saga()
        if  tus == '7':     el.ac_kapa_adimla(+1)
        if  tus == '8':     el.ac_kapa_adimla(-1)

