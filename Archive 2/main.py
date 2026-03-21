import tkinter as tk
import logging
from gui import Gui

#logging configuration so erros get printed to the console
logging.basicConfig(level=logging.INFO, format="%(name)s - %(levelname)s - %(message)s")

if __name__ == "__main__":
    #tk entry point
    window = tk.Tk()
    app = Gui(window)
    window.mainloop()