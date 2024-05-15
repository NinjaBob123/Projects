import time
from time import sleep
from tkinter import *
import random

class Window:
    def printFood(self, evt):
        for x in self.array:
            for y in self.array[x]:
                if "food" in self.array[x][y]:
                    print(f"({x}, {y})")

    def getNum(self):
        self.num = self.array[self.pos[0]][self.pos[1]]

    def draw(self):
        self.character.grid_forget()
        self.character.grid(column=self.pos[0], row=self.pos[1])
        self.character.config(bg="green")
        self.count += 0.01
        if self.count >= 60:
            self.minutes = self.count / 60
            self.seconds = self.count - (minutes * 60)
        else:
            self.seconds = self.count
        self.time.set(f"{self.minutes}: {self.seconds}")
        self.score.set(f"Score is: {self.size}")
        self.lvlStr.set(f"Level {self.level}")
        self.win.update()
        self.win.update_idletasks()

    def moveUp(self, evt):
        self.pos = (self.pos[0], self.pos[1] - 1)
        self.draw()
        self.getNum()
        try:
            if "food" in self.array[self.pos[0]][self.pos[1]]:
                raise KeyError
            self.filler[str(self.num).replace(" food", "")].grid(column=self.pos[0], row=self.pos[1] + 1)
            hold = self.array[self.pos[0]][self.pos[1] + 1]
            self.array[self.pos[0]][self.pos[1] + 1] = self.array[self.pos[0]][self.pos[1]]
            self.array[self.pos[0]][self.pos[1]] = hold
            self.draw()
        except KeyError:
            self.filler[str(self.num).replace(" food", "")] = self.filler[str(self.num)]
            self.filler[str(self.num).replace(" food", "")].grid(column=self.pos[0], row=self.pos[1] + 1)
            hold = self.array[self.pos[0]][self.pos[1] + 1].replace(" food", "")
            self.array[self.pos[0]][self.pos[1] + 1] = self.array[self.pos[0]][self.pos[1]].replace(" food", "")
            self.array[self.pos[0]][self.pos[1]] = hold
            self.draw()
            self.filler[str(self.num)].config(bg="black")
            self.size += 1
            print(f"Size is now: {self.size}")
            self.foodCount -= 1
            print(self.foodCount)
        self.draw()
        print(self.pos)

    def moveLeft(self, evt):
        self.pos = (self.pos[0] - 1, self.pos[1])
        self.draw()
        self.getNum()
        try:
            if "food" in self.array[self.pos[0]][self.pos[1]]:
                raise KeyError
            self.filler[str(self.num).replace(" food", "")].grid(column=self.pos[0] + 1, row=self.pos[1])
            hold = self.array[self.pos[0] + 1][self.pos[1]]
            self.array[self.pos[0] + 1][self.pos[1]] = self.array[self.pos[0]][self.pos[1]]
            self.array[self.pos[0]][self.pos[1]] = hold
            self.draw()
        except KeyError:
            self.filler[str(self.num).replace(" food", "")] = self.filler[str(self.num)]
            self.filler[str(self.num).replace(" food", "")].grid(column=self.pos[0] + 1, row=self.pos[1])
            hold = self.array[self.pos[0] + 1][self.pos[1]].replace(" food", "")
            self.array[self.pos[0] + 1][self.pos[1]] = self.array[self.pos[0]][self.pos[1]].replace(" food", "")
            self.array[self.pos[0]][self.pos[1]] = hold
            self.draw()
            self.filler[str(self.num)].config(bg="black")
            self.size += 1
            print(f"Size is now: {self.size}")
            self.foodCount -= 1
            print(self.foodCount)
        self.draw()
        print(self.pos)

    def moveRight(self, evt):
        self.pos = (self.pos[0] + 1, self.pos[1])
        self.draw()
        self.getNum()
        try:
            if "food" in self.array[self.pos[0]][self.pos[1]]:
                raise KeyError
            self.filler[str(self.num).replace(" food", "")].grid(column=self.pos[0] - 1, row=self.pos[1])
            hold = self.array[self.pos[0] - 1][self.pos[1]]
            self.array[self.pos[0] - 1][self.pos[1]] = self.array[self.pos[0]][self.pos[1]]
            self.array[self.pos[0]][self.pos[1]] = hold
            self.draw()
        except KeyError:
            print("Found Food!")
            self.filler[str(self.num).replace(" food", "")] = self.filler[str(self.num)]
            self.filler[str(self.num).replace(" food", "")].grid(column=self.pos[0] - 1, row=self.pos[1])
            hold = self.array[self.pos[0] - 1][self.pos[1]].replace(" food", "")
            self.array[self.pos[0] - 1][self.pos[1]] = self.array[self.pos[0]][self.pos[1]].replace(" food", "")
            self.array[self.pos[0]][self.pos[1]] = hold
            self.draw()
            self.filler[str(self.num)].config(bg="black")
            self.size += 1
            print(f"Size is now: {self.size}")
            self.foodCount -= 1
            print(self.foodCount)
        self.draw()
        print(self.pos)

    def moveDown(self, evt):
        self.pos = (self.pos[0], self.pos[1] + 1)
        self.draw()
        self.getNum()
        try:
            if "food" in self.array[self.pos[0]][self.pos[1]]:
                raise KeyError
            self.filler[str(self.num).replace(" food", "")].grid(column=self.pos[0], row=self.pos[1] - 1)
            hold = self.array[self.pos[0]][self.pos[1] - 1]
            self.array[self.pos[0]][self.pos[1] - 1] = self.array[self.pos[0]][self.pos[1]]
            self.array[self.pos[0]][self.pos[1]] = hold
            self.draw()
        except KeyError:
            self.filler[str(self.num)].config(bg="black")
            self.size += 1
            self.filler[str(self.num).replace(" food", "")] = self.filler[str(self.num)]
            self.filler[str(self.num).replace(" food", "")].grid(column=self.pos[0], row=self.pos[1] - 1)
            hold = self.array[self.pos[0]][self.pos[1] - 1].replace(" food", "")
            self.array[self.pos[0]][self.pos[1] - 1] = self.array[self.pos[0]][self.pos[1]].replace(" food", "")
            self.array[self.pos[0]][self.pos[1]] = hold
            self.draw()
            print(f"Size is now: {self.size}")
            self.foodCount -= 1
            print(self.foodCount)
        self.draw()
        print(self.pos)

    def start(self):
        self.starter.destroy()
        self.scrLbl = Label(self.win, textvariable=self.score, fg='white', bg='black')
        self.lvlLbl = Label(self.win, textvariable=self.lvlStr, fg='white', bg='black')
        self.timeLbl = Label(self.win, textvariable=self.time, fg='white', bg='black')
        self.scrLbl.grid(column=0, row=0)
        self.lvlLbl.grid(column=0, row=1)
        self.timeLbl.grid(column=0, row=2)
        self.win.update()
        sleep(0.01)
        self.win.update()
        self.win.update_idletasks()
        self.character = Frame(self.frame, bg="green", width="10", height="10")
        self.character.grid(column=24, row=24)
        num = 0
        for x in range(50):
            self.array[x] = {}
            for y in range(50):
                num1 = random.randint(0, 101)
                if num1 == 10:
                    self.filler[str(num) + " food"] = Frame(self.frame, bg="red", width="10", height="10")
                    if not x == 24 or not y == 24:
                        self.filler[str(num) + " food"].grid(column=x, row=y)
                        self.array[x][y] = str(num) + " food"
                        num += 1
                        self.foodCount += 1
                    elif x == 24 and y == 24:
                        self.array[x][y] = "character"
                else:
                    self.filler[str(num)] = Frame(self.frame, width="10", height="10", background='')
                    if not x == 24 or not y == 24:
                        self.filler[str(num)].grid(column=x, row=y)
                        self.array[x][y] = str(num)
                        num += 1
                    elif x == 24 and y == 24:
                        self.array[x][y] = "character"
        self.bool = True
        print(self.array)

    def __init__(self):
        self.newTime = None
        self.oldTime = None
        self.character = None
        self.bool = False
        self.scrLbl = None
        self.num = None
        self.lvlLbl = None
        self.timeLbl = None
        self.count = 0
        self.time = StringVar()
        self.level = 1
        self.lvlStr = StringVar()
        self.foodCount = 0
        self.array = {}
        self.size = 0
        self.win = Tk()
        self.win.grid()
        self.score = StringVar()
        self.score.set(f"Score is: {self.size}")
        self.frame = Frame(self.win, bg='black')
        self.frame.grid(column=1, row=0)
        self.win.geometry("600x500")
        self.win.configure(bg="black")
        self.win.title("Hunters Snake Game")
        self.starter = Button(self.frame, text="start", command=self.start, bg="red")
        self.starter.grid(column=1, row=1)
        self.pos = (24, 24)
        self.filler = {}
        self.win.bind("<Up>", self.moveUp)
        self.win.bind("<Left>", self.moveLeft)
        self.win.bind("<Right>", self.moveRight)
        self.win.bind("<Down>", self.moveDown)
        self.win.bind("p", self.printFood)
        self.win.bind("P", self.printFood)

    def generate(self):
        self.level += 1
        self.bool = False
        for x in self.array:
            for y in self.array[x]:
                try:
                    test = int(self.array[x][y])
                    self.filler[self.array[x][y]].destroy()
                except ValueError:
                    self.pos = (24, 24)
                    self.character.grid_forget()
        countdown = 2
        label = Label(self.frame, text=f"Level {self.level}", fg="green", bg="black", font="Ariel 50")
        label.pack()
        self.win.update()
        self.win.update_idletasks()
        while countdown != 0:
            countdown -= 1
            sleep(1)
        label.destroy()
        num = 0
        for x in range(50):
            self.array[x] = {}
            for y in range(50):
                num1 = random.randint(0, 101)
                if num1 == 10:
                    self.filler[str(num) + " food"] = Frame(self.frame, bg="red", width="10", height="10")
                    if not x == 24 or not y == 24:
                        self.filler[str(num) + " food"].grid(column=x, row=y)
                        self.array[x][y] = str(num) + " food"
                        num += 1
                        self.foodCount += 1
                    elif x == 24 and y == 24:
                        self.array[x][y] = "character"
                else:
                    self.filler[str(num)] = Frame(self.frame, width="10", height="10", background='')
                    if not x == 24 or not y == 24:
                        self.filler[str(num)].grid(column=x, row=y)
                        self.array[x][y] = str(num)
                        num += 1
                    elif x == 24 and y == 24:
                        self.array[x][y] = "character"
        self.bool = True
        self.draw()
        print(self.array)


w = Window()
frame = w.frame
while 1:
    frame.update()
    frame.update_idletasks()
    if w.bool:
        w.draw()
        if w.foodCount == 0:
            w.generate()
    sleep(0.01)
