from visual import *
import math

class El:
    def ac_kapa_adimla(self, yon=+1):
        hiz = math.radians(self.hiz)                # (acisal) 'hiz' deg/sn -> rad/sn
        MAX_ROT_ANG = pi / 7                        # max donme acisi
        ANGLE = yon * MAX_ROT_ANG / self.STEP_SIZE  # aci adimlari
        AXIS  = (0, 0, 1)                           # donme ekseni

        print self.step, self.STEP_SIZE
        if (math.fabs(self.step) < self.STEP_SIZE) or (yon * self.step == - self.STEP_SIZE):
            self.fthumb_prox.rotate   (angle=0.6*ANGLE, axis=(0,1,0))
            self.fthumb_middle.rotate (angle=0.6*ANGLE, axis=(0,1,0))
            self.fthumb_distal.rotate (angle=0.6*ANGLE, axis=(0,1,0))

            self.findex_prox.rotate   (angle=ANGLE, axis=AXIS)
            self.findex_middle.rotate (angle=ANGLE, axis=AXIS)
            self.findex_distal.rotate (angle=ANGLE, axis=AXIS)

            self.fmiddle_prox.rotate  (angle=ANGLE, axis=AXIS)
            self.fmiddle_middle.rotate(angle=ANGLE, axis=AXIS)
            self.fmiddle_distal.rotate(angle=ANGLE, axis=AXIS)

            self.fring_prox.rotate    (angle=ANGLE, axis=AXIS)
            self.fring_middle.rotate  (angle=ANGLE, axis=AXIS)
            self.fring_distal.rotate  (angle=ANGLE, axis=AXIS)

            self.fpinky_prox.rotate   (angle=ANGLE, axis=AXIS)
            self.fpinky_middle.rotate (angle=ANGLE, axis=AXIS)
            self.fpinky_distal.rotate (angle=ANGLE, axis=AXIS)

            self.step = self.step + yon

        if self.step == yon * self.STEP_SIZE:
            self.DURUM = self.ACIK
        elif self.step == 0:
            self.DURUM = self.SERBEST
        else:
            self.DURUM = self.KAPALI

    def ac_kapa(self, yon=+1):
        hiz = math.radians(self.hiz)                # (acisal) 'hiz' deg/sn -> rad/sn
        MAX_ROT_ANG = pi / 7                        # max donme acisi
        ANGLE = yon * MAX_ROT_ANG / self.STEP_SIZE  # aci adimlari
        RATE  = math.fabs(hiz / ANGLE)              # donme yenileme frekansi

        for i in range(self.STEP_SIZE):
            rate(RATE)

            self.ac_kapa_adimla(yon)

    def asagi_yukari(self, yon=+1):
        hiz = math.radians(self.hiz)                # (acisal) 'hiz' deg/sn -> rad/sn
        MAX_ROT_ANG = 1.5 * pi / 7                  # max donme acisi
        ANGLE = yon * MAX_ROT_ANG / self.STEP_SIZE  # aci adimlari
        RATE  = math.fabs(hiz / ANGLE)              # donme yenileme frekansi
        AXIS  = (0, 0, 1)                           # donme ekseni

        for i in range(self.STEP_SIZE):
            rate(RATE)

            self.fpalm.rotate         (angle=ANGLE, axis=AXIS)

    def saga_sola_dondur(self, yon=+1):
        hiz = math.radians(self.hiz)            # (acisal) 'hiz' deg/sn -> rad/sn
        MAX_ROT_ANG = -1.5 * pi / 7             # max donme acisi
        STEP_SIZE = 100                         # adim sayisi:
                                                # donme acikligi kac parca
        ANGLE = yon * MAX_ROT_ANG / STEP_SIZE   # aci adimlari
        RATE  = math.fabs(hiz / ANGLE)          # donme yenileme frekansi
        AXIS  = (0, 1, 0)                       # donme ekseni

        for i in range(STEP_SIZE):
            rate(RATE)

            self.fpalm.rotate(angle=ANGLE, axis=AXIS)

    def serbest(self):
        if self.DURUM == self.ACIK:
            self.ac_kapa(+1)
        elif self.DURUM == self.KAPALI:
            self.ac_kapa(-1)
        elif self.DURUM == self.YUKARI:
            self.asagi_yukari(-1)
        elif self.DURUM == self.ASAGI:
            self.asagi_yukari(+1)
        elif self.DURUM == self.SOLA:
            self.saga_sola_dondur(-1)
        elif self.DURUM == self.SAGA:
            self.saga_sola_dondur(+1)

        self.DURUM = self.SERBEST

    def ac(self):
        if self.DURUM <> self.ACIK:
            self.serbest()
            self.ac_kapa(-1)
            self.DURUM = self.ACIK

    def kapa(self):
        if self.DURUM <> self.KAPALI:
            self.serbest()
            self.ac_kapa(+1)
            self.DURUM = self.KAPALI

    def yukari(self):
        if self.DURUM <> self.YUKARI:
            self.serbest()
            self.asagi_yukari(+1)
            self.DURUM = self.YUKARI

    def asagi(self):
        if self.DURUM <> self.ASAGI:
            self.serbest()
            self.asagi_yukari(-1)
            self.DURUM = self.ASAGI

    def sola(self):
        if self.DURUM <> self.SOLA:
            self.serbest()
            self.saga_sola_dondur(+1)
            self.DURUM = self.SOLA

    def saga(self):
        if self.DURUM <> self.SAGA:
            self.serbest()
            self.saga_sola_dondur(-1)
            self.DURUM = self.SAGA

    def __init__(self, name, color=color.red, hiz=25, scene=None):
        if scene != None:
            scene.select()

        # Base frame
        self.__body = frame()
        fbody = self.__body

        self.hiz = hiz      # (acisal) hiz: deg/sn
        self.SERBEST, self.ACIK, self.KAPALI, self.YUKARI, self.ASAGI, self.SOLA, self.SAGA = range(0, 7, 1)
        self.STEP_SIZE = 100
        self.step = self.STEP_SIZE

        # frame ler
        self.fkol  = frame(frame=fbody, axis=(0, 1, 0))
        self.fpalm = frame(frame=fbody, pos=(0, -12.3, 3.8))

        self.fthumb_prox    = frame(frame=self.fpalm,          pos=(0,  5.8,  -4.8), axis=(2, 4, -3))
        self.fthumb_middle  = frame(frame=self.fthumb_prox,    pos=(4.5,  0,     0))
        self.fthumb_distal  = frame(frame=self.fthumb_middle,  pos=(2.5,  0,     0))

        self.findex_prox    = frame(frame=self.fpalm,          pos=(0,  12.3, -3.8), axis=(1, 5, 0))
        self.findex_middle  = frame(frame=self.findex_prox,    pos=(4.5,   0,    0))
        self.findex_distal  = frame(frame=self.findex_middle,  pos=(2.5,   0,    0))

        self.fmiddle_prox   = frame(frame=self.fpalm,          pos=(0, 12.3, -3.8), axis=(1, 5, 0))
        self.fmiddle_middle = frame(frame=self.fmiddle_prox,   pos=(5,    0,    0))
        self.fmiddle_distal = frame(frame=self.fmiddle_middle, pos=(3,    0,    0))

        self.fring_prox     = frame(frame=self.fpalm,          pos=(0,  12.3, -3.8), axis=(1, 5, 0))
        self.fring_middle   = frame(frame=self.fring_prox,     pos=(4.7,   0,    0))
        self.fring_distal   = frame(frame=self.fring_middle,   pos=(2.8,   0,    0))

        self.fpinky_prox    = frame(frame=self.fpalm,          pos=(0,  12.3, -3.8), axis=(1, 5, 0))
        self.fpinky_middle  = frame(frame=self.fpinky_prox,    pos=(3.5,   0,    0))
        self.fpinky_distal  = frame(frame=self.fpinky_middle,  pos=(2.4,   0,    0))

        # nesneler
        self.kol   = cylinder (frame=self.fkol , pos=(-31, 0, 3),    length=20,  radius=3.5)
        self.palm  = box      (frame=self.fpalm, pos=(0, 8.8,    0),    length=2,   height=9,  width=10)
        self.palme = ellipsoid(frame=self.fpalm, pos=(0,   7,    0),    length=2,   height=13, width=11)

        self.thumb_prox    = cylinder(frame=self.fthumb_prox,    radius=1, length = 4.5)
        self.thumb_middle  = cylinder(frame=self.fthumb_middle,  radius=1, length = 2.5)
        self.thumb_distal  = cylinder(frame=self.fthumb_distal,  radius=1, length = 2)

        self.index_prox    = cylinder(frame=self.findex_prox,    radius=1, length = 4.5)
        self.index_middle  = cylinder(frame=self.findex_middle,  radius=1, length = 2.5)
        self.index_distal  = cylinder(frame=self.findex_distal,  radius=1, length = 2)

        self.middle_prox   = cylinder(frame=self.fmiddle_prox,   radius=1, length = 5,   pos = (0, 0, 2.5))
        self.middle_middle = cylinder(frame=self.fmiddle_middle, radius=1, length = 3,   pos = (0, 0, 2.5))
        self.middle_distal = cylinder(frame=self.fmiddle_distal, radius=1, length = 2.2, pos = (0, 0, 2.5))

        self.ring_prox     = cylinder(frame=self.fring_prox,     radius=1, length = 4.7, pos = (0, 0, 5))
        self.ring_middle   = cylinder(frame=self.fring_middle,   radius=1, length = 2.8, pos = (0, 0, 5))
        self.ring_distal   = cylinder(frame=self.fring_distal,   radius=1, length = 2,   pos = (0, 0, 5))

        self.pinky_prox    = cylinder(frame=self.fpinky_prox,    radius=1, length = 3.5, pos = (0, 0, 7.5))
        self.pinky_middle  = cylinder(frame=self.fpinky_middle,  radius=1, length = 2.4, pos = (0, 0, 7.5))
        self.pinky_distal  = cylinder(frame=self.fpinky_distal,  radius=1, length = 1.9, pos = (0, 0, 7.5))

        # parmak uclari
        self.thumb_uc  = sphere(frame=self.fthumb_distal,  radius=1, pos=(2.3, 0, 0))
        self.index_uc  = sphere(frame=self.findex_distal,  radius=1, pos=(2.3, 0, 0))
        self.middle_uc = sphere(frame=self.fmiddle_distal, radius=1, pos=(2.6, 0, 2.5))
        self.ring_uc   = sphere(frame=self.fring_distal,   radius=1, pos=(2.4, 0, 5))
        self.pinky_uc  = sphere(frame=self.fpinky_distal,  radius=1, pos=(2.3, 0, 7.5))

        self.ac_kapa(-1)
        self.DURUM = self.SERBEST

    def setColor(self, color):
        for obj in self.__body.objects:
            obj.color = color

    def setPosition(self, position):
        self.__body.pos = position

    def setAxis(self, axis):
        self.__body.axis = axis

