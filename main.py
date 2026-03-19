import tkinter as tk
from gui import Gui

if __name__ == "__main__":
    #tk entry point
    window = tk.Tk()
    app = Gui(window)
    window.mainloop()