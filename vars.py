from tkinter import Tk, Canvas, BOTH, ALL



selfWindow = Tk()
selfCanvas = Canvas(selfWindow)
selfWindow.title("Welcome to modelator window!")
selfWindow.geometry("600x600")
selfWindow.resizable(False, False)
selfCanvas.focus_set()



rotationx, rotationy, rotationz = 0, 0, 0