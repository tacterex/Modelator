from tkinter import Tk, Canvas, Button, BOTH



class startWindow(Tk):
    def __init__(self):
        super().__init__()
        self.buildself()
        self.mainloop()
    
    def buildself(self):
        self.title("start")
        for i in range(4):
            obj = Button(self,
                text=f"{i+1}D", height = 2, width = 35, justify="center",
                command=None
            )   
            obj.pack()
            self.resizable(False, False)



class buildWindow(Tk):
    def __init__(self):
        super().__init__()
        selfCanvas = Canvas(self)

    def buildself(self):
        self.geometry("600x700")
        self.cubeButton = Button(text = "Cube")




if __name__ == "__main__":
    app = startWindow()