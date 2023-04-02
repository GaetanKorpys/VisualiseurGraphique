from PIL import Image, ImageTk
import tkinter as tk
from ivy.ivy import *
from ivy.std_api import *

from VisualiseurGraphique import VisualiseurGraphique

if __name__ == '__main__':

    root = tk.Tk()
    visualiseurGraphique = VisualiseurGraphique(root)
    root.mainloop()





