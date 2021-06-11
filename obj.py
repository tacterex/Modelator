from tkinter import Tk, Canvas
import tkinter as tk
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
            x0, y0, x1, y1 = self.x, self.y, self.x+self.a, self.y-self.a
            self.verts = [[x0, y0], [x0, y1], [x1, y1], [x1, y0]]
            self.canvas.create_rectangle(self.x, self.y, self.x+self.a, self.y-self.a, width=3)
        else:
            temp = polus((AXES[self.n-1][3] - AXES[self.n-1][1]) / (AXES[self.n-1][0] - AXES[self.n-1][2]))
            self.verts = Square(self.canvas, self.n-1, self.x, self.y, self.a) + Square(self.canvas, self.n-1, self.x+1/SQRT2*self.a, self.y-temp/SQRT2*self.a, self.a)

    def __add__(self, other):
        self.buildself()
        other.buildself()
        for vert in range(len(self.verts)):
            self.canvas.create_line(
                self.verts[vert][0], self.verts[vert][1], other.verts[vert][0], other.verts[vert][1], arrow=tk.LAST, width=3
            )
        temp = []
        for elem in self.verts:
            temp.append(elem)
        for elem in other.verts:
            temp.append(elem)
        return temp