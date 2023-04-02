import tkinter as tk
import math
from queue import Queue
import sys
from GUI import GUI
from PIL import Image, ImageTk
from ivy.ivy import *
from ivy.std_api import *
import time
import threading
import random
from Turtle import Turtle


class VisualiseurGraphique():

    def on_message(agent):
        info("Received from %r: %s", agent)

    def on_connetion_change(agent, event, *args):
        if event == IvyApplicationDisconnected:
            print("Ivy application %r has disconnected", agent)
        else:
            print("Ivy application %r has connected", agent)
            print("Ivy application currently on the bus: %s", ",".join(IvyGetApplicationList()))

    def on_die(agent, id):
        #info("Received the order to die from %r with id = %d", agent, id)
        print("Received the order to die from %r with id = %d", agent, id)
        IvyStop()

    def addToQueue(self, *args):
        self.queue.put(args[1])


    def __init__(self, master):

        self.master = master
        self.queue = Queue()
        self.gui = GUI(self.master, self.queue, self.endApplication)

        self.running = 1
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()

        self.periodicCall()


    def periodicCall(self):
        """
        Check every 100 ms if there is something new in the queue.
        """
        self.gui.processIncoming()

        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            IvyStop()
            sys.exit(0)

        self.master.after(100, self.periodicCall)


    def workerThread1(self):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select()'.
        One important thing to remember is that the thread has to yield
        control.
        """

        IvyInit("Visualiseur Graphique Agent", "Visualiseur Graphique est pret", 0, self.on_connetion_change, self.on_die)
        IvyStart("127.0.0.1:2010")
        IvyBindMsg(self.addToQueue, "(^AVANCE [1-9][0-9]?$|^AVANCE 100$)")
        IvyBindMsg(self.addToQueue, "(^RECULE [1-9][0-9]?$|^RECULE 100$)")
        IvyBindMsg(self.addToQueue, "(^TOURNEDROITE (?:36[0]|3[0-5][0-9]|[12][0-9][0-9]|[1-9]?[0-9])?$)")
        IvyBindMsg(self.addToQueue, "(^TOURNEGAUCHE (?:36[0]|3[0-5][0-9]|[12][0-9][0-9]|[1-9]?[0-9])?$)")
        IvyBindMsg(self.addToQueue, "(^LEVECRAYON$)")
        IvyBindMsg(self.addToQueue, "(^BAISSECRAYON$)")
        IvyBindMsg(self.addToQueue, "(^ORIGINE$)")
        IvyBindMsg(self.addToQueue, "(^RESTAURE$)")
        IvyBindMsg(self.addToQueue, "(^NETTOIE$)")
        IvyBindMsg(self.addToQueue, "(^FCC (?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5]) (?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5]) (?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])$)")
        IvyBindMsg(self.addToQueue, "(^FCAP (?:36[0]|3[0-5][0-9]|[12][0-9][0-9]|[1-9]?[0-9])?$)")
        IvyBindMsg(self.addToQueue, "(^FPOS.*)")


    def endApplication(self):
        self.running = 0




