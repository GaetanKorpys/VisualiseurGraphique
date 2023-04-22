import tkinter as tk
import math
from ivy.ivy import *

from RegexCommand import RegexCommand
from Turtle import Turtle


class GUI():
    def __init__(self, master, queue, endCommand):

        # Import regex commands
        self.regexCommand = RegexCommand()

        self.queue = queue
        self.master = master
        self.canvas = tk.Canvas(self.master, bg="white", width=800, height=600)
        self.canvas.pack()

        console = tk.Button(self.master, text='Close', command=endCommand)
        console.pack()

        self.master.update()

        x = self.canvas.winfo_width() / 2
        y = self.canvas.winfo_height() / 2

        self.turtle = Turtle(x, y, -90)
        self.displayTurtle(self.turtle)


    def processIncoming(self):
        """
        Handle all the messages currently in the queue (if any).
        """
        while self.queue.qsize():
            if not self.queue.empty():
                msg = self.queue.get()
                self.readCmdFromQueue(msg)


    def readCmdFromQueue(self, command):

        if re.match(self.regexCommand.avancerRegex, command):

            old_x = self.turtle.x
            old_y = self.turtle.y

            message_parts = command.split(" ")
            nb = message_parts[1]
            nb = int(nb)
            self.turtle.avance(nb)

            self.canvas.move(self.turtleSprite, self.turtle.x - old_x, self.turtle.y - old_y)

            color = self.rgbToColor(self.turtle.couleur)

            if not self.turtle.crayon_leve:
                self.canvas.create_line(old_x, old_y, self.turtle.x, self.turtle.y, fill=color)



        elif re.match(self.regexCommand.reculerRegex, command):

            old_x = self.turtle.x
            old_y = self.turtle.y

            message_parts = command.split(" ")
            nb = message_parts[1]
            nb = int(nb)
            self.turtle.recule(nb)

            self.canvas.move(self.turtleSprite, self.turtle.x - old_x, self.turtle.y - old_y)

            color = self.rgbToColor(self.turtle.couleur)

            if not self.turtle.crayon_leve:
                self.canvas.create_line(old_x, old_y, self.turtle.x, self.turtle.y, fill=color)

        elif re.match(self.regexCommand.tourneDroiteRegex, command):

            message_parts = command.split(" ")
            angle = message_parts[1]
            angle = int(angle)

            self.turtle.tourne_droite(angle)

            self.rotate(angle)

        elif re.match(self.regexCommand.tourneGaucheRegex, command):

            message_parts = command.split(" ")
            angle = message_parts[1]
            angle = int(angle)

            self.turtle.tourne_gauche(angle)

            self.rotate(-angle)

        elif re.match(self.regexCommand.leveCrayonRegex, command):

            self.turtle.leve_crayon()

        elif re.match(self.regexCommand.baisseCrayonRegex, command):

            self.turtle.baisse_crayon()

        elif re.match(self.regexCommand.origineRegex, command):

            self.turtle.origine()
            self.canvas.delete(self.turtleSprite)
            self.displayTurtle(self.turtle)

        elif re.match(self.regexCommand.restaureRegex, command):

            self.turtle.restaure()
            self.canvas.delete("all")
            self.displayTurtle(self.turtle)

        elif re.match(self.regexCommand.nettoieRegex, command):

            self.canvas.delete("all")
            self.displayTurtle(self.turtle)


        elif re.match(self.regexCommand.fccRegex, command):

            message_parts = command.split(" ")

            r = int(message_parts[1])
            g = int(message_parts[2])
            b = int(message_parts[3])

            self.turtle.fcc(r, g, b)


        elif re.match(self.regexCommand.fcapRegex, command):

            message_parts = command.split(" ")
            direction = message_parts[1]

            self.turtle.fcap(-int(direction))
            self.canvas.delete(self.turtleSprite)
            self.displayTurtle(self.turtle)

        elif re.match(self.regexCommand.fposRegex, command):

            message_parts = command.split(" ")
            x = message_parts[1]
            y = message_parts[2]

            self.turtle.fpos(int(x), int(y))
            self.canvas.delete(self.turtleSprite)
            self.displayTurtle(self.turtle)

    def rgbToColor(self, rgb):
        return "#%02x%02x%02x" % rgb

    def setDirectionTurtle(self, angle):
        self.rotate(angle)

    def displayTurtle(self, turtle):
        x = turtle.x
        y = turtle.y

        size = 10
        points = [x - size, y + size, x + size + 7 , y, x-size, y - size]

        color = self.rgbToColor(self.turtle.couleur)
        # Create the triangle on the canvas
        self.turtleSprite = self.canvas.create_polygon(points, fill=color)
        self.rotate(self.turtle.angle)


    def rotate(self, angle):
        # get the current coordinates of the turtle sprite
        coords = self.canvas.coords(self.turtleSprite)
        old_x = (coords[0] + coords[2]) / 2
        old_y = (coords[1] + coords[3]) / 2

        self.canvas.coords(self.turtleSprite, *self.rotate_coords(coords, old_x, old_y, math.radians(angle)))


    def rotate_coords(self, coords, x, y, radian_angle):

        # loop through the coordinates of the turtle sprite and apply the rotation
        rotated_coords = []
        for i in range(0, len(coords), 2):
            # get the x and y coordinates of the point to rotate
            x_coord = coords[i]
            y_coord = coords[i + 1]

            # calculate the new x and y coordinates after rotation
            new_x = (x_coord - x) * math.cos(radian_angle) - (y_coord - y) * math.sin(radian_angle) + x
            new_y = (x_coord - x) * math.sin(radian_angle) + (y_coord - y) * math.cos(radian_angle) + y

            # add the rotated point to the list of rotated coordinates
            rotated_coords.extend([new_x, new_y])

        return rotated_coords


