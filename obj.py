from tkinter import Canvas
import tkinter as tk
import math

SQRT2 = math.sqrt(2)
SQRT3 = math.sqrt(3)

SIGN = lambda a: a/abs(a) if a!= 0 else 0

def AXES(n):
    arr = [
        [0, 300, 600, 300],
        [10, 600, 10, 0]
    ]
    tempAngle = 90/((n+1)//2)
    delta = 1
    for i in range(n-2):
        angle = -90+tempAngle*(i+delta)
        if angle == 0:
            delta+=1
            angle = -90+tempAngle*(i+delta)
        sign = SIGN(angle)
        angle = abs(angle)
        t = math.tan(math.radians(angle))
        if t >= 0.5:
            arr.append([10, 300, 300/t, 300+sign*300])
        else:
            arr.append([10, 300, 600, 300+sign*300*t])
    return arr

cosFormTg = lambda a, b: abs(b)/math.sqrt(a**2 + b**2)
sinFromTg = lambda a, b: abs(a)/math.sqrt(a**2 + b**2)


class Square:
    def __init__(self, canvas:Canvas, n, pointx, pointy, size, level=1, color=None, axs=None):
        self.axes = axs
        self.color = color
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
            self.canvas.create_rectangle(self.x, self.y, self.x+self.a, self.y-self.a, width=1, outline=self.color)
        else:
            a = self.axes[self.n-1][3] - self.axes[self.n-1][1]
            b = self.axes[self.n-1][0] - self.axes[self.n-1][2]
            sign  = SIGN(a/b)
            sin = sinFromTg(a, b)
            cos = cosFormTg(a, b)
            if self.level == 1:
                self.verts = Square(self.canvas, self.n-1, self.x, self.y, self.a, self.level-1, "red", self.axes) + Square(self.canvas, self.n-1, self.x+cos*self.a, self.y-sign*sin*self.a, self.a, self.level-1, "blue", self.axes)
            elif self.level < 1:
                self.verts = Square(self.canvas, self.n-1, self.x, self.y, self.a, self.level-1, self.color, self.axes) + Square(self.canvas, self.n-1, self.x+cos*self.a, self.y-sign*sin*self.a, self.a, self.level-1, self.color, self.axes)

    def __add__(self, other):
        self.buildself()
        other.buildself()
        for vert in range(len(self.verts)):
            self.canvas.create_line(
                self.verts[vert][0], self.verts[vert][1], other.verts[vert][0], other.verts[vert][1],
                arrow=tk.LAST if self.level==0 else None, width=1, fill=self.color if self.level < 0 else None
            )
        temp = []
        for elem in self.verts:
            temp.append(elem)
        for elem in other.verts:
            temp.append(elem)
        return temp



class Simplex:
    def __init__(self, canvas:Canvas, n, pointx, pointy, size, level=1, color=None, axs=None):
        self.canvas = canvas
        self.axes = axs
        self.level = level
        self.color = color
        self.n = n
        self.x, self.y = pointx, pointy
        self.h = size
        self.verts = []
        self.buildself()
    
    def buildself(self):
        if self.n==2:
            self.verts = [[self.x-self.h/SQRT3, self.y+self.h/3], [self.x+self.h/SQRT3, self.y+self.h/3], [self.x, self.y-self.h*2/3]]
            self.canvas.create_line(self.verts[0], self.verts[1], fill=self.color)
            self.canvas.create_line(self.verts[1], self.verts[2], fill=self.color)
            self.canvas.create_line(self.verts[2], self.verts[0], fill=self.color)
            self.canvas.create_oval(
                self.x-3, self.y-3, self.x+3, self.y+3, fill="black"
            )
        else:
            temp = Simplex(self.canvas, self.n-1, self.x, self.y, self.h, self.level-1, "red", self.axes)
            a = self.axes[self.n-1][3] - self.axes[self.n-1][1]
            b = self.axes[self.n-1][0] - self.axes[self.n-1][2]
            sign  = SIGN(a/b)
            sin = sinFromTg(a, b)
            cos = cosFormTg(a, b)
            point = [self.x+self.h*cos, self.y-self.h*sin*sign]
            for p in temp.verts:
                self.canvas.create_line(p, point, fill=self.color if self.level<1 else "blue")
            self.verts = temp.verts
            self.verts.append(point)
            if self.level == 1:
                self.canvas.create_line(self.x, self.y, point, dash=(2,2))