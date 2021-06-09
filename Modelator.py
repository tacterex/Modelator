from tkinter import Tk, Canvas, BOTH, ALL
import math
import keyboard



SQRT2 = math.sqrt(2)
SQRT3 = math.sqrt(3)
selfWindow = Tk()
selfCanvas = Canvas(selfWindow)

rotationx, rotationy, rotationz = 0, 0, 25

def init():
    selfWindow.title("Welcome to modelator window!")
    selfWindow.geometry("600x600")
def rebuild(rx, ry, rz):
    selfCanvas.delete(ALL)
    rx, ry, rz = rx%360, ry%360, rz%360
    if 0 <= rz <= 90:
        selfCanvas.create_rectangle(
            0, 300-300*rz/90, 600, 300+300*rz/90,
            outline="black", fill="lightgray"
        )
def update():
    rebuild(rotationx, rotationy, rotationz)
    selfCanvas.pack(fill=BOTH, expand=1)
    selfWindow.mainloop()