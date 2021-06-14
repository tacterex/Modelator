from tkinter import Tk, Canvas, Button, BOTH, font
import tkinter as tk
import obj
#test comment


class infoWindow(Tk):
    def __init__(self, shape):
        super().__init__()
        self.shape = shape
        self.buildself()
    
    def buildself(self):
        self.geometry("300x300")
        self.title("Info")
def callInfo(text):
    psevdoApp = infoWindow(text)


HYPERCUBE = "HyperCube"
SIMPLEX = "Simplex"



class buildWindow(Tk):
    def __init__(self, n=1):
        super().__init__()
        self.n = n
        self.selfCanvas = Canvas(self, width=600, height=600, background="lightgray")
        self.buildself()
        self.selfCanvas.pack(fill=BOTH, expand=1)

    def buildself(self):
        self.geometry("1200x700")
        self.resizable(False, False)
        self.title(f"{self.n}D window")
        self.CubeButton = Button(self, text = "HyperCube",
        justify="center", font="Arial 24",
        command=lambda: self.__spawnShape(HYPERCUBE)
        )
        self.CubeButton.place(x=0, y=600, width = 300, height = 100)
        self.CubeInfoBt = Button(self, text = "Get Info",
        justify="center", font="Arial 24", command=lambda: callInfo(HYPERCUBE)
        )
        self.CubeInfoBt.place(x=300,y=600,width=300,height=100)
        self.SimplexButton = Button(self, text = "Simplex",
        font="Arial 24", justify="center",
        command=lambda: self.__spawnShape(SIMPLEX)
        )
        self.SimplexButton.place(x=600, y=0, width=300, height=100)
        self.SimplexInfoBt = Button(self, text = "Get Info",
        justify="center", font="Arial 24", command=lambda: callInfo(SIMPLEX)
        )
        self.SimplexInfoBt.place(x=300,y=600,width=300,height=100)
        #
        self.__buildAxes()

    def __buildAxes(self):
        self.selfCanvas.delete(tk.ALL)
        for i in range(self.n):
            self.selfCanvas.create_line(obj.AXES(self.n)[i], arrow = tk.LAST, width = 0.5)
    
    def __spawnShape(self, shape):
        self.__buildAxes()
        if shape == HYPERCUBE:
            obj.Square(self.selfCanvas, self.n, 10, 300, 80,  axs=obj.AXES(self.n))
        elif shape == SIMPLEX:
            obj.Simplex(self.selfCanvas, self.n, 70, 265, 100, axs=obj.AXES(self.n))
        
    

def d2():
    currentWindow = buildWindow(2)
def d3():
    currentWindow = buildWindow(3)
def d4():
    currentWindow = buildWindow(4)
def d5():
    currentWindow = buildWindow(5)
def d6():
    currentWindow = buildWindow(6)
def d7():
    currentWindow = buildWindow(7)
def d8():
    currentWindow = buildWindow(8)
def d9():
    currentWindow = buildWindow(9)
def d10():
    currentWindow = buildWindow(10)
funs = [d2, d3, d4, d5, d6, d7, d8, d9, d10]



class startWindow(Tk):
    def __init__(self):
        super().__init__()
        self.buildself()
        self.mainloop()
    
    def buildself(self):
        self.title("start")
        for i in range(9):
            obj = Button(self,
                text=f"{i+2}D", height = 2, width = 35, justify="center",
                command=funs[i]
            )   
            obj.pack()
            self.resizable(False, False)




if __name__ == "__main__":
    app = startWindow()