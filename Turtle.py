import math

class Turtle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.crayon_leve = False
        self.couleur = (0, 0, 0)

    def avance(self, pas):
        radian = math.radians(self.angle)
        self.x += pas * math.cos(radian)
        self.y += pas * math.sin(radian)

    def recule(self, pas):
        radian = math.radians(self.angle)
        self.x -= pas * math.cos(radian)
        self.y -= pas * math.sin(radian)

    def tourne_droite(self, angle):
        self.angle = (self.angle + angle) % 360

    def tourne_gauche(self, angle):
        self.angle = (self.angle - angle) % 360

    def leve_crayon(self):
        self.crayon_leve = True

    def baisse_crayon(self):
        self.crayon_leve = False

    def origine(self):
        self.x = 0
        self.y = 0

    def restaure(self):
        self.x = 0
        self.y = 0
        self.angle = 90
        self.crayon_leve = False
        self.couleur = (0, 0, 0)

    def fcc(self, r, g, b):
        self.couleur = (r, g, b)

    def fcap(self, angle):
        self.angle = angle

    def fpos(self, x, y):
        self.x = x
        self.y = y

    def getPos(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
