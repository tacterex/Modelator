from tkinter import Tk, Canvas, BOTH, ALL
import math
import vars



SQRT2 = math.sqrt(2)
SQRT3 = math.sqrt(3)

def rotx(t):
    if t == "Up":
        vars.rotationx -= 1
    elif t == "Down":
        vars.rotationx += 1
    rebuild()

def rebuild():
    vars.selfCanvas.delete(ALL)
    rx, ry, rz = vars.rotationx % 360, vars.rotationy % 360, vars.rotationz % 360
    if -90 <= rx <= 90:
        vars.selfCanvas.create_rectangle(
            0, 300-300*rx/90, 600, 300+300*rx/90,
            outline="black", fill="lightgray"
        )

def update():
    rebuild()
    vars.selfCanvas.pack(fill=BOTH, expand=1)
    vars.selfCanvas.bind("<w>", lambda k: rotx("Up"))
    vars.selfCanvas.bind("<s>", lambda k: rotx("Down"))
    vars.selfWindow.mainloop()