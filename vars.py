from tkinter import Tk, Canvas, Button, BOTH



#
curWindow = {"n": None, "window": None, "canvas": None}
def openWindow(index):
    curWindow["n"] = index+1
    curWindow["window"] = Tk()
    curWindow["canvas"] = Canvas(curWindow["window"])
    curWindow["window"].geometry("600x600")
    curWindow["window"].title(f"{index+1}D window")
#



startWindow = Tk()
startWindow.title("start")
for i in range(4):
    obj = Button(startWindow,
        text=f"{i+1}D", height = 2, width = 35, justify="center",
        command=lambda: openWindow(i)
    )
    obj.pack()
startWindow.resizable(False, False)