import tkinter as tk
from gui import Gui

if __name__ == "__main__":
    window = tk.Tk()
    app = Gui(window)
    window.mainloop()