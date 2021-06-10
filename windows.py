from tkinter import Tk, Canvas, Button, BOTH, PhotoImage, LEFT



class buildWindow(Tk):
    def __init__(self, n=1):
        super().__init__()
        self.n = n
        self.selfCanvas = Canvas(self, width=600, height=600)
        self.PIXELVIRTUAL = PhotoImage(width = 1, height = 1)
        self.buildself()
    def buildself(self):
        self.geometry("600x700")
        self.resizable(False, False)
        self.title(f"{self.n}D window")
        self.CubeButton = Button(self, text = "Cube",
        image = self.PIXELVIRTUAL, width  = 300, height = 100, justify="center"
        )
        self.CubeButton.pack()

currentWindow = {"n": None, "window": None, "canvas": None}
def d2():
    currentWindow["n"] = 2
    currentWindow["window"] = buildWindow(currentWindow["n"])
    currentWindow["canvas"] = currentWindow["window"].selfCanvas
def d3():
    currentWindow["n"] = 3
    currentWindow["window"] = buildWindow(currentWindow["n"])
    currentWindow["canvas"] = currentWindow["window"].selfCanvas
def d4():
    currentWindow["n"] = 4
    currentWindow["window"] = buildWindow(currentWindow["n"])
    currentWindow["canvas"] = currentWindow["window"].selfCanvas
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
            obj.pack(side=LEFT)
            self.resizable(False, False)




if __name__ == "__main__":
    app = startWindow()