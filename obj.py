from tkinter import Tk, Canvas
import tkinter as tk
import math

SQRT2 = math.sqrt(2)
SQRT3 = math.sqrt(3)

AXES = [
    [5, 300, 600, 300],
    [5, 600, 5, 0],


    [5, 300, 97.476, 0],

    [5, 300, 217.963, 0],
    
    [5, 300, 412.915, 0],

    [5, 300, 600, 105.048],
    [5, 300, 600, 494.952],

    [5, 300, 412.915, 600],

    [5, 300, 217.963, 600],

    [5, 300, 97.476, 600]
]

print(len(AXES))

SIGN = lambda a: a/abs(a)

cosFormTg = lambda a, b: abs(b)/math.sqrt(a**2 + b**2)
sinFromTg = lambda a, b: abs(a)/math.sqrt(a**2 + b**2)


class Square:
    def __init__(self, canvas:Canvas, n, pointx, pointy, size, level=1):
        self.canvas = canvas
        self.n = n
        self.x, self.y = pointx, pointy
        self.a = abs(size)
        self.verts = []
        self.level = level
        self.buildself()
    
    def buildself(self):
        if self.n == 2:
            x0, y0, x1, y1 = self.x, self.y, self.x+self.a, self.y-self.a
            self.verts = [[x0, y0], [x0, y1], [x1, y1], [x1, y0]]
            self.canvas.create_rectangle(self.x, self.y, self.x+self.a, self.y-self.a, width=1)
        else:
            a = AXES[self.n-1][3] - AXES[self.n-1][1]
            b = AXES[self.n-1][0] - AXES[self.n-1][2]
            sign  = SIGN(a/b)
            sin = sinFromTg(a, b)
            cos = cosFormTg(a, b)
            self.verts = Square(self.canvas, self.n-1, self.x, self.y, self.a, self.level-1) + Square(self.canvas, self.n-1, self.x+cos*self.a, self.y-sign*sin*self.a, self.a, self.level-1)

    def __add__(self, other):
        self.buildself()
        other.buildself()
        for vert in range(len(self.verts)):
            self.canvas.create_line(
                self.verts[vert][0], self.verts[vert][1], other.verts[vert][0], other.verts[vert][1], arrow=tk.LAST if self.level==0 else None, width=1
            )
        temp = []
        for elem in self.verts:
            temp.append(elem)
        for elem in other.verts:
            temp.append(elem)
        return temp