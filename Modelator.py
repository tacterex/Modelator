from tkinter import Tk, Canvas, BOTH
import math



SQRT2 = math.sqrt(2)
SQRT3 = math.sqrt(3)
selfWindow = Tk()
selfCanvas = Canvas(selfWindow)
def init():
    selfWindow.title("Welcome to modelator window!")
    selfWindow.geometry("600x600")
def update():
    selfCanvas.pack(fill=BOTH, expand=1)
    selfWindow.mainloop()