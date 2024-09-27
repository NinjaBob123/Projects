from tkinter import *
from time import sleep
class Window:
  def __init__(self):
    self.window = Tk()
    self.window.geometry = "500x500"
  def mainloop(self):
    self.window.update()
    self.window.update_idletasks()
    sleep(0.01)
class Game:
  def __init__(self):
    w = Window()
    self.window = w.window
