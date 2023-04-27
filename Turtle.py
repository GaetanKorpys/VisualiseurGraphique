import math

class Turtle:

    def __init__(self, xStart, yStart, angleStart):
        ''' Constructeur '''
        self.xStart = xStart
        self.yStart = yStart
        self.angleStart = angleStart
        self.x = self.xStart
        self.y = self.yStart
        self.angle = self.angleStart
        self.crayon_leve = False
        self.couleur = (0, 0, 0)


    def avance(self, pas):
        ''' Avance la tortue selon un nombre de pas '''
        radian = math.radians(self.angle)
        self.x += pas * math.cos(radian)
        self.y += pas * math.sin(radian)


    def recule(self, pas):
        ''' Recule la tortue selon un nombre de pas '''
        radian = math.radians(self.angle)
        self.x -= pas * math.cos(radian)
        self.y -= pas * math.sin(radian)


    def tourne_droite(self, angle):
        ''' Fait pivoter la tortue vers la droite selon un angle '''
        self.angle = (self.angle + angle) % 360


    def tourne_gauche(self, angle):
        ''' Fait pivoter la tortue vers la gauche selon un angle '''
        self.angle = (self.angle - angle) % 360


    def leve_crayon(self):
        ''' Lève le crayon de la tortue'''
        self.crayon_leve = True


    def baisse_crayon(self):
        ''' Baisse le crayon de la tortue'''
        self.crayon_leve = False


    def origine(self):
        ''' Replace la tortue à la position d'origine'''
        self.x = self.xStart
        self.y = self.yStart


    def restaure(self):
        ''' Replace la tortue à son état inital et efface le dessin'''
        self.x = self.xStart
        self.y = self.yStart
        self.angle = self.angleStart
        self.crayon_leve = False
        self.couleur = (0, 0, 0)


    def fcc(self, r, g, b):
        ''' Modifie la couleur du crayon'''
        self.couleur = (r, g, b)


    def fcap(self, angle):
        ''' Modifie la direction de la tortue'''
        self.angle = angle


    def fpos(self, x, y):
        ''' Modifie la position de la tortue'''
        self.x = x
        self.y = y


    def getPos(self):
        ''' Return la position de la tortue (str)'''
        return "(" + str(self.x) + ", " + str(self.y) + ")"

