from tkinter import Tk, Canvas
import math

SQRT2 = math.sqrt(2)
SQRT3 = math.sqrt(3)

class Square:
    def __init__(self, canvas:Canvas, n, pointx, pointy, size):
        self.canvas = canvas
        self.n = n
        self.x, self.y = pointx, pointy
        self.a = abs(size)
        self.buildself()
    
    def buildself(self):
        if self.n == 2:
            self.canvas.create_rectangle(
                self.x-self.a/2, self.y-self.a/2, self.x+self.a/2, self.y+self.a/2
            )