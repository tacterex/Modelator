from tkinter import Tk, Canvas, Button, BOTH
import tkinter as tk
import obj



class buildWindow(Tk):
    def __init__(self, n=1):
        super().__init__()
        self.n = n
        self.selfCanvas = Canvas(self, width=600, height=600, background="lightgray")
        self.buildself()
        self.selfCanvas.pack(fill=BOTH, expand=1)

    def buildself(self):
        self.geometry("600x700")
        self.resizable(False, False)
        self.title(f"{self.n}D window")
        self.CubeButton = Button(self, text = "Square",
        justify="center", font="Arial 26",
        command=lambda: obj.Square(self.selfCanvas, self.n, 300, 300, 50)
        )
        self.CubeButton.place(x=0, y=600, width = 600, height = 100)
        #self.CircleButton = Button(self, text = "Circle",
        #justify="center", font="Arial 26"
        #)
        #self.CircleButton.place(x=300, y=600, width = 300, height = 100)
        #self.quitButton = Button(
            #self, text="Quit", command=lambda: quit(), justify="center", font="Arial 26"
        #)
        #self.quitButton.place(x=0, y=700, width=600, height=100)
        #
        for i in range(self.n):
            self.selfCanvas.create_line(obj.AXES[i], arrow = tk.LAST)

    

def d2():
    currentWindow = buildWindow(2)
def d3():
    currentWindow = buildWindow(3)
def d4():
    currentWindow = buildWindow(4)
funs = [d2, d3, d4]



class startWindow(Tk):
    def __init__(self):
        super().__init__()
        self.buildself()
        self.mainloop()
    
    def buildself(self):
        self.title("start")
        for i in range(3):
            obj = Button(self,
                text=f"{i+2}D", height = 2, width = 35, justify="center",
                command=funs[i]
            )   
            obj.pack()
            self.resizable(False, False)




if __name__ == "__main__":
    app = startWindow()