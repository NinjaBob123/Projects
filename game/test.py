from tkinter import *
import time
frame = Tk()
frame.grid()
test1 = Label(frame, text="Watch me move!")
test1.grid(column=0, row=0)
test2 = Label(frame, text="I am switching places")
test2.grid(column=0, row=1)
topBool = True
while 1:
    if topBool:
        test1.grid(column=0, row=1)
        test2.grid(column=0, row=0)
    else:
        test1.grid(column=0, row=0)
        test2.grid(column=0, row=1)
    frame.update()
    frame.update_idletasks()
    time.sleep(5)
