from queue import Queue
from GUI import GUI
from ivy.std_api import *
import threading

from RegexCommand import RegexCommand


class VisualiseurGraphique():

    def __init__(self, master):

        # Import regex commands
        self.regexCommand = RegexCommand()

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

        IvyInit("VisualiseurGraphiqueAgent", "Visualiseur Graphique est pret", 0, self.on_connetion_change, self.on_die)
        IvyStart()
        IvyBindMsg(self.addToQueue, "("+self.regexCommand.avancerRegex+")")
        IvyBindMsg(self.addToQueue, "("+self.regexCommand.reculerRegex+")")
        IvyBindMsg(self.addToQueue, "("+self.regexCommand.tourneDroiteRegex+")")
        IvyBindMsg(self.addToQueue, "("+self.regexCommand.tourneGaucheRegex+")")
        IvyBindMsg(self.addToQueue, "("+self.regexCommand.leveCrayonRegex+")")
        IvyBindMsg(self.addToQueue, "("+self.regexCommand.baisseCrayonRegex+")")
        IvyBindMsg(self.addToQueue, "("+self.regexCommand.origineRegex+")")
        IvyBindMsg(self.addToQueue, "("+self.regexCommand.restaureRegex+")")
        IvyBindMsg(self.addToQueue, "("+self.regexCommand.nettoieRegex+")")
        IvyBindMsg(self.addToQueue, "("+self.regexCommand.fccRegex+")")
        IvyBindMsg(self.addToQueue, "("+self.regexCommand.fcapRegex+")")
        IvyBindMsg(self.addToQueue, "("+self.regexCommand.fposRegex+")")


    def endApplication(self):
        self.running = 0

    def addToQueue(self, *args):
        self.queue.put(args[1])

    def on_connetion_change(agent, event, *args):
        if event == IvyApplicationDisconnected:
            # info("Ivy application %r has disconnected", agent)
            print("Ivy application %r has disconnected", agent)
        else:
            # info("Ivy application %r has connected", agent)
            # info("Ivy application currently on the bus: %s", ",".join(IvyGetApplicationList()))
            print("Ivy application %r has connected", agent)
            print("Ivy application currently on the bus: %s", ",".join(IvyGetApplicationList()))

    def on_die(agent, id):
        #info("Received the order to die from %r with id = %d", agent, id)
        print("Received the order to die from %r with id = %d", agent, id)
        IvyStop()
