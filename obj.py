from tkinter import Tk, Canvas

class Square:
    def __init__(self, canvas:Canvas, n, pointx, pointy, size):
        self.canvas = canvas
        self.n = n
        self.image = None
        self.x, self.y = pointx, pointy
        self.a = abs(size)
        self.buildself()
    
    def buildself(self):
        if self.n == 2:
            self.image = self.canvas.create_rectangle(
                self.x-self.a/2, self.y-self.a/2, self.x+self.a/2, self.y+self.a/2
            )