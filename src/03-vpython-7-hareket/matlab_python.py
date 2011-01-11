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
       el.yuk()
    elif num == 2:
       el.asg()
    elif num == 3:
       el.ac()
    elif num == 4:
       el.kapa()
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

scene = display( title='Bilek Ac/Kapa', autoscale=0, background=(123, 134, 76))
scene.height = scene.width = 600
scene.center = (-2,0,0)

el = El(scene=scene, name="El", hiz=5)

el.setPosition((0, 0, 0))

thefile = open('test.txt')
lines = follow(thefile)

for line in lines:
    process(line)

