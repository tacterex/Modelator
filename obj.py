from tkinter import Tk, Canvas
import math

SQRT2 = math.sqrt(2)
SQRT3 = math.sqrt(3)

AXES = [
    [0, 300, 600, 300],
    [300, 600, 300, 0],
    [0, 600, 600, 0],
    [0, 0, 600, 600]
]

polus = lambda a: a/abs(a)

class Square:
    def __init__(self, canvas:Canvas, n, pointx, pointy, size):
        self.canvas = canvas
        self.n = n
        self.x, self.y = pointx, pointy
        self.a = abs(size)
        self.verts = []
        self.buildself()
    
    def buildself(self):
        if self.n == 2:
            self.verts = [self.x, self.y, self.x+self.a, self.y+self.a]
            self.canvas.create_rectangle(self.verts)
        else:
            temp = polus((AXES[self.n][3] - AXES[self.n][1]) / (AXES[self.n][0] - AXES[self.n][2]))
            Square(self.canvas, self.n-1, self.x, self.y, self.a) + Square(self.canvas, self.n-1, self.x+temp*SQRT2*self.a, self.y-temp*SQRT2*self.a, self.a)

    def __add__(self, other):
        self.buildself()
        other.buildself()