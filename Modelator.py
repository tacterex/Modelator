from tkinter import Tk, Canvas, BOTH, ALL
import math
import vars



SQRT2 = math.sqrt(2)
SQRT3 = math.sqrt(3)

DWP = lambda a, b: 0 if a==0 else (a/abs(a))*abs(a)%b

def rotx(t):
    if t == "Up":
        vars.rotationx -= 1
    elif t == "Down":
        vars.rotationx += 1
    rebuild()

def rebuild():
    vars.selfCanvas.delete(ALL)
    rx, ry, rz = DWP(vars.rotationx, 360), DWP(vars.rotationy, 360), DWP(vars.rotationz, 360)
    if -90 <= rx <= 90:
        vars.selfCanvas.create_rectangle(
            0, 300-300*rx/90, 600, 300+300*rx/90,
            outline="black", fill="whitesmoke"
        )
        if rx != 0:
            for i in range(int(300-300*rx/90), int(300+300*rx/90), int(6*rx/18)):
                vars.selfCanvas.create_line(
                    0, i, 600, i,
                    dash=(4,4)
                )

def update():
    rebuild()
    vars.selfCanvas.pack(fill=BOTH, expand=1)
    vars.selfCanvas.bind("<w>", lambda k: rotx("Up"))
    vars.selfCanvas.bind("<s>", lambda k: rotx("Down"))
    vars.selfWindow.mainloop()