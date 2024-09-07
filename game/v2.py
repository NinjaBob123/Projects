import time
from time import sleep
from tkinter import *
import random
from math import *


class Window:
    def getTime(self):
        got = time.time()
        elapsed = fabs(self.startTime - got)
        if elapsed >= 60:
            minutes = round(elapsed / 60)
            seconds = fabs(round(elapsed - (minutes * 60), 2))
        else:
            minutes = 0
            seconds = fabs(round(elapsed))
        return f"{minutes}: {seconds}"

    def printFood(self, evt):
        test = False
        for x in self.array:
            for y in self.array[x]:
                if "food" in self.array[x][y]:
                    test = True
                    print(f"({x}, {y})")
        if not test:
            self.foodCount = 0

    def getNum(self):
        self.num = self.array[self.pos[0]][self.pos[1]]

    def getTileNum(self, x, y):
        self.gotNum = self.array[x][y]

    def draw(self):
        self.character.grid_forget()
        for x in self.prePos:
            self.getTileNum(x[0], x[1])
            if self.gotNum != 'character':
                self.filler[self.gotNum].configure(bg="black")
        self.character.grid(column=self.pos[0], row=self.pos[1])
        self.character.config(bg="green")
        if self.length >= 1:
            num = 0
            num2 = 0
            breaker = False
            for x in self.prePos:
                if num >= self.length:
                    if not breaker:
                        for y in self.prePos:
                            if num2 > self.length:
                                self.getTileNum(y[0], y[1])
                                if self.gotNum != 'character':
                                    self.filler[self.gotNum].configure(bg="black")
                            num2 += 1
                        breaker = True
                if breaker:
                    break
                self.getTileNum(x[0], x[1])
                if self.gotNum != 'character':
                    self.filler[self.gotNum].configure(bg="green")
                num += 1

        self.score.set(f"Score is: {self.size}")
        self.win.update()
        self.win.update_idletasks()

    def moveUp(self, evt):
        self.prePos.insert(0, self.pos)
        print(self.prePos)
        self.pos = (self.pos[0], self.pos[1] - 1)
        if self.pos[0] <= -1:
            self.pos = (49, self.pos[1])
        elif self.pos[0] >= 50:
            self.pos = (0, self.pos[1])
        if self.pos[1] <= -1:
            self.pos = (self.pos[0], 49)
        elif self.pos[1] >= 50:
            self.pos = (self.pos[0], 0)

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
            self.length += 1
            print(f"Size is now: {self.size}")
            self.foodCount -= 1
            print(self.foodCount)
        self.draw()
        print(self.pos)

    def moveLeft(self, evt):
        self.prePos.insert(0, self.pos)
        print(self.prePos)
        self.pos = (self.pos[0] - 1, self.pos[1])
        if self.pos[0] <= -1:
            self.pos = (49, self.pos[1])
        elif self.pos[0] >= 50:
            self.pos = (0, self.pos[1])
        if self.pos[1] <= -1:
            self.pos = (self.pos[0], 49)
        elif self.pos[1] >= 50:
            self.pos = (self.pos[0], 0)
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
            self.length += 1
            print(f"Size is now: {self.size}")
            self.foodCount -= 1
            print(self.foodCount)
        self.draw()
        print(self.pos)

    def moveRight(self, evt):
        self.prePos.insert(0, self.pos)
        print(self.prePos)
        self.pos = (self.pos[0] + 1, self.pos[1])
        if self.pos[0] <= -1:
            self.pos = (49, self.pos[1])
        elif self.pos[0] >= 50:
            self.pos = (0, self.pos[1])
        if self.pos[1] <= -1:
            self.pos = (self.pos[0], 49)
        elif self.pos[1] >= 50:
            self.pos = (self.pos[0], 0)
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
            self.length += 1
            print(f"Size is now: {self.size}")
            self.foodCount -= 1
            print(self.foodCount)
        self.draw()
        print(self.pos)

    def moveDown(self, evt):
        self.prePos.insert(0, self.pos)
        print(self.prePos)
        self.pos = (self.pos[0], self.pos[1] + 1)
        if self.pos[0] <= -1:
            self.pos = (49, self.pos[1])
        elif self.pos[0] >= 50:
            self.pos = (0, self.pos[1])
        if self.pos[1] <= -1:
            self.pos = (self.pos[0], 49)
        elif self.pos[1] >= 50:
            self.pos = (self.pos[0], 0)
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
            self.length += 1
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
        self.startTime = time.time()
        self.starter.destroy()
        self.scrLbl = Label(self.win, textvariable=self.score, fg='white', bg='black')
        self.scrLbl.grid(column=0, row=0)
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
        self.gotNum = None
        self.startTime = None
        self.character = None
        self.bool = False
        self.scrLbl = None
        self.num = None
        self.level = 1
        self.foodCount = 0
        self.array = {}
        self.size = 0
        self.length = 0
        self.win = Tk()
        self.win.grid()
        self.score = StringVar()
        self.score.set(f"Score is: {self.size}")
        self.frame = Frame(self.win, bg='black')
        self.frame.grid(column=1, row=0)
        self.win.geometry("600x500")
        self.win.configure(bg="black")
        self.win.title("Hunters Game")
        self.starter = Button(self.frame, text="start", command=self.start, bg="red")
        self.starter.grid(column=1, row=1)
        self.pos = (24, 24)
        self.prePos = []
        self.charDict = {}
        self.filler = {}
        self.win.bind("<Up>", self.moveUp)
        self.win.bind("<Left>", self.moveLeft)
        self.win.bind("<Right>", self.moveRight)
        self.win.bind("<Down>", self.moveDown)
        self.win.bind("p", self.printFood)
        self.win.bind("P", self.printFood)

    def generate(self):
        self.prePos = []
        self.level += 1
        self.bool = False
        for x in self.array:
            for y in self.array[x]:
                try:
                    test = int(self.array[x][y])
                    try:
                        self.filler[self.array[x][y]].destroy()
                    except KeyError:
                        self.filler[self.array[x][y] + " food"].destroy()
                except ValueError:
                    self.pos = (24, 24)
                    self.character.grid_forget()
        countdown = 2
        label = Label(self.frame, text=f"Level {self.level}", fg="green", bg="black", font="Ariel 50")
        label2 = Label(self.frame, text=f"Time elapsed: {self.getTime()}", fg="white", bg="black", font="Ariel 25")
        label.pack()
        label2.pack()
        self.win.update()
        self.win.update_idletasks()
        while countdown != 0:
            countdown -= 1
            sleep(1)
        label.destroy()
        label2.destroy()
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
