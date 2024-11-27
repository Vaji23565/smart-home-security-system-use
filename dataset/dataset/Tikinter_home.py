from tkinter import *
from tkinter import messagebox
from functools import partial
from detect import detectcam
from trainer import trainimage
from face_recog import captureimage

def launchapp():
    tkWindow = Tk()  
    tkWindow.geometry('500x350')  
    tkWindow.title('Home Security system')
    tkWindow.configure(bg='black')

    # Capture Image button
    capturebutton = Button(tkWindow, text="Capture Image", command=captureimage).grid(row=1, column=10)
    # Train Images Button
    trainButton = Button(tkWindow, text="trainimages", command=trainimage).grid(row=3, column=10)
    # Detect person button
    detectButton = Button(tkWindow, text="Detect", command=detectcam).grid(row=5, column=10)  

    tkWindow.mainloop()
