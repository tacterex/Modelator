from tkinter import Tk, Canvas, BOTH, ALL
import math
import keyboard



SQRT2 = math.sqrt(2)
SQRT3 = math.sqrt(3)
selfWindow = Tk()
selfCanvas = Canvas(selfWindow)
selfWindow.title("Welcome to modelator window!")
selfWindow.geometry("600x600")
selfWindow.resizable(False, False)
selfCanvas.focus_set()

def init():
    global rotationx, rotationy, rotationz
    rotationx, rotationy, rotationz = 0, 0, 0

def rotx(t):
    global rotationx
    if t == "Up":
        rotationx -= 1
    elif t == "Down":
        rotationx += 1
    rebuild()

def rebuild():
    global rotationx, rotationy, rotationz
    selfCanvas.delete(ALL)
    rx, ry, rz = rotationx%360, rotationy%360, rotationz%360
    if -90 <= rx <= 90:
        selfCanvas.create_rectangle(
            0, 300-abs(300*rx/90), 600, 300+abs(300*rx/90),
            outline="black", fill="lightgray"
        )

def update():
    rebuild()
    selfCanvas.pack(fill=BOTH, expand=1)
    selfCanvas.bind("<w>", lambda k: rotx("Up"))
    selfCanvas.bind("<s>", lambda k: rotx("Down"))
    selfWindow.mainloop()