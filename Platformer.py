import tkinter as tk
import time
from random import *
from builtins import Exception

"""""""""
class Gravity():
    def __init__():
        self.force = int()
        self.grav = -9
    def cal(force):
        self.afterForce = force + self.grav
""""""""""
class CancelJump(Exception):
    def __init__(self, message=None, data=None, *args):
        super(Exception, self).__init__(message, *args)
        self.data = data


win = tk.Tk()
win.grid()
root = tk.Canvas(win, width=500, height=357, bd=0, highlightthickness=0)
root.grid(column=0, row=0)


class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


def within_x(co1, co2):
    if ((co2.x1 < co1.x1 < co2.x2)
            or (co2.x1 < co1.x2 < co2.x2)
            or (co2.x1 > co1.x1 and co1.x2 < co2.x2)
            or (co2.x2 > co1.x1 > co1.x2)):
        return True
    else:
        return False


def within_y(co1, co2):
    if ((co2.y1 < co1.y1 < co2.y2)
            or (co2.y1 < co1.y2 < co2.y2)
            or (co2.y1 > co1.y1 and co1.y2 < co2.y2)
            or (co2.y2 > co1.y1 > co1.y2)):
        return True
    else:
        return False


def collided(co1, co2):
    if within_x(co1, co2) and within_y(co1, co2):
        return True


class Player:
    def __init__(self, canvas, platform):
        self.canvas = canvas
        self.head = root.create_oval(20, 20, 50, 50, fill='grey')
        self.legA = root.create_line(35, 50, 45, 65)
        self.legB = root.create_line(45, 65, 35, 80)
        self.canvas.move(self.head, 40, 200)
        self.canvas.move(self.legA, 40, 200)
        self.canvas.move(self.legB, 40, 200)
        self.y = 0
        win.bind('<Key>', self.jump)
        self.platform = platform
        self.touchBool = bool()
        self.pos = Coords()
        self.platAPos = Coords()
        self.platBPos = Coords()
        self.platCPos = Coords()
        self.platA = self.platform.platA
        self.platB = self.platform.platB
        self.platC = self.platform.platC
        self.platPosLst = [self.platAPos, self.platBPos, self.platCPos]
        self.platLst = [self.platA, self.platB, self.platC]

    def posGet(self):
        self.pos.x1 = self.canvas.coords(self.legB)[0]
        self.pos.y1 = self.canvas.coords(self.legB)[1]
        self.pos.x2 = self.canvas.coords(self.legB)[2]
        self.pos.y2 = self.canvas.coords(self.legB)[3]
        self.platAPos.x1 = self.canvas.coords(self.platform.platA)[0]
        self.platAPos.y1 = self.canvas.coords(self.platform.platA)[1]
        self.platAPos.x2 = self.canvas.coords(self.platform.platA)[2]
        self.platAPos.y2 = self.canvas.coords(self.platform.platA)[3]
        self.platBPos.x1 = self.canvas.coords(self.platform.platB)[0]
        self.platBPos.y1 = self.canvas.coords(self.platform.platB)[1]
        self.platBPos.x2 = self.canvas.coords(self.platform.platB)[2]
        self.platBPos.y2 = self.canvas.coords(self.platform.platB)[3]
        self.platCPos.x1 = self.canvas.coords(self.platform.platC)[0]
        self.platCPos.y1 = self.canvas.coords(self.platform.platC)[1]
        self.platCPos.x2 = self.canvas.coords(self.platform.platC)[2]
        self.platCPos.y2 = self.canvas.coords(self.platform.platC)[3]

    def draw(self):
        self.canvas.move(self.head, 0, self.y)
        self.canvas.move(self.legA, 0, self.y)
        self.canvas.move(self.legB, 0, self.y)
        self.posGet()
        if self.platTouch() and self.y != 0:
            print('not bropken')
            self.y = 0
        if self.y < 0:
            self.jumpTime += 1
            if self.jumpTime > 100:
                self.y = 2
        # print("self: {}, platA: {}, platB: {}, platC: {}".format(self.pos, self.platAPos, self.platBPos, self.platCPos))

    def jump(self, event):
        if event.char == 'w':
            if self.y == 0:
                self.y = -1
                self.jumpTime = 0

    def platTouch(self):
        global i
        self.posGet()
        for x in self.platPosLst:
            if collided(self.pos, x):
                i = True
                break
        if i:
            return True
        else:
            return False


class Platforms:
    def __init__(self, canvas):
        self.canvas = canvas
        self.platA = root.create_rectangle(-20, 80, 80, 100)
        self.platB = root.create_rectangle(-20, 80, 80, 100)
        self.platC = root.create_rectangle(-20, 80, 80, 100)
        self.canvas.move(self.platA, 40, 200)
        self.canvas.move(self.platB, 240, randint(100, 250))
        self.canvas.move(self.platC, 440, randint(100, 250))


platform = Platforms(root)
player = Player(root, platform)

while 1:
    player.draw()
    if player.y == -1:
        player.y = 0
        if player.platTouch():
            pass
        else:
            player.y = -1
    win.update_idletasks()
    win.update()
    time.sleep(0.00001)
    print(player.y)
