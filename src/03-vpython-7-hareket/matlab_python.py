from El import *
from visual import display, color, scene
import time

durum = 0

def process(line):
    global durum
    # do something
    print line
    num = int(line)

    if  num == 1:
       el.ac()
    elif num == 2:
       el.kapa()
    elif num == 3:
       el.yukari()
    elif num == 4:
        el.asagi()
    elif num == 7:
        el.ac_kapa_adimla(+1)
    elif num == 8:
        el.ac_kapa_adimla(-1)
    else:
        print "yok boyle bir sey"

    durum = num

def follow(thefile):
    thefile.seek(0,2)		# go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)	# sleep briefly
            continue
        yield line

#clearscreen()

scene = display( title='Bilek Ac/Kapa', background=(1,1,0))

#scene = display( title='Bilek Ac/Kapa', autoscale=0, background=(123, 134, 76))
scene.height = scene.width = 300
scene.center = (-2,0,0)

el = El(scene=scene, name="El", hiz=25)

el.setPosition((0, 0, 0))

thefile = open('test.txt')
lines = follow(thefile)

for line in lines:
    print line
    process(line)

