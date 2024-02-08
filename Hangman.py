import _tkinter
import random
from tkinter import *
import time

wordLst = ['askew', 'galaxy', 'mnemonic', 'syndrome', 'thriftless', 'topaz', 'vaporize', 'camera', 'ceiling']  # add more words
endBool = bool()
g = None
while 1:
    class Game:
        def __init__(self):
            self.win = Tk()
            self.win.title('Hangman Game')
            self.win.resizable(0, 0)
            self.win.grid()
            self.root = Canvas(self.win, height=500, width=500)
            self.root.grid(column=0, row=0)
            self.win.update()
            self.k = None
            self.h = None
        def mainloop(self):
            self.k = Keyboard()
            self.h = Hangman(self.k, self.root)
            while True:
                self.h.getLetter()
                self.win.update_idletasks()
                self.win.update()
                if endBool:
                    break
                time.sleep(0.01)

    try:
        if not isinstance(g, Game):
            g = Game()
            endBool = False
        else:
            pass
    except NameError:
        g = Game
    class Keyboard:
        def __init__(self):
            self.root = Frame(g.win, height=300, width=600, bg='grey')
            self.root.grid(column=1, row=0)
            self.a = Button(self.root, text='A', command=lambda: self.letterChange('a'))
            self.b = Button(self.root, text='B', command=lambda: self.letterChange('b'))
            self.c = Button(self.root, text='C', command=lambda: self.letterChange('c'))
            self.d = Button(self.root, text='D', command=lambda: self.letterChange('d'))
            self.e = Button(self.root, text='E', command=lambda: self.letterChange('e'))
            self.f = Button(self.root, text='F', command=lambda: self.letterChange('f'))
            self.g = Button(self.root, text='G', command=lambda: self.letterChange('g'))
            self.h = Button(self.root, text='H', command=lambda: self.letterChange('h'))
            self.i = Button(self.root, text='I', command=lambda: self.letterChange('i'))
            self.j = Button(self.root, text='J', command=lambda: self.letterChange('j'))
            self.k = Button(self.root, text='K', command=lambda: self.letterChange('k'))
            self.l = Button(self.root, text='L', command=lambda: self.letterChange('l'))
            self.m = Button(self.root, text='M', command=lambda: self.letterChange('m'))
            self.n = Button(self.root, text='N', command=lambda: self.letterChange('n'))
            self.o = Button(self.root, text='O', command=lambda: self.letterChange('o'))
            self.p = Button(self.root, text='P', command=lambda: self.letterChange('p'))
            self.q = Button(self.root, text='Q', command=lambda: self.letterChange('q'))
            self.r = Button(self.root, text='R', command=lambda: self.letterChange('r'))
            self.s = Button(self.root, text='S', command=lambda: self.letterChange('s'))
            self.t = Button(self.root, text='T', command=lambda: self.letterChange('t'))
            self.u = Button(self.root, text='U', command=lambda: self.letterChange('u'))
            self.v = Button(self.root, text='V', command=lambda: self.letterChange('v'))
            self.w = Button(self.root, text='W', command=lambda: self.letterChange('w'))
            self.x = Button(self.root, text='X', command=lambda: self.letterChange('x'))
            self.y = Button(self.root, text='Y', command=lambda: self.letterChange('y'))
            self.z = Button(self.root, text='Z', command=lambda: self.letterChange('z'))
            self.a.grid(column=0, row=1)
            self.b.grid(column=4, row=2)
            self.c.grid(column=2, row=2)
            self.d.grid(column=2, row=1)
            self.e.grid(column=2, row=0)
            self.f.grid(column=3, row=1)
            self.g.grid(column=4, row=1)
            self.h.grid(column=5, row=1)
            self.i.grid(column=7, row=0)
            self.j.grid(column=6, row=1)
            self.k.grid(column=7, row=1)
            self.l.grid(column=8, row=0)
            self.m.grid(column=6, row=2)
            self.n.grid(column=5, row=2)
            self.o.grid(column=7, row=2)
            self.p.grid(column=8, row=1)
            self.q.grid(column=0, row=0)
            self.r.grid(column=3, row=0)
            self.s.grid(column=1, row=1)
            self.t.grid(column=4, row=0)
            self.u.grid(column=6, row=0)
            self.v.grid(column=3, row=2)
            self.w.grid(column=1, row=0)
            self.x.grid(column=1, row=2)
            self.y.grid(column=5, row=0)
            self.z.grid(column=0, row=2)
            self.letter = str()

        def letterChange(self, newLetter: str):
            self.letter = newLetter
            g.h.getLetter()
            g.h.checkLetter()


    class Hangman:
        def __init__(self, keyboard, canvas):
            random.shuffle(wordLst)
            self.word = wordLst[0]
            self.canvas = canvas
            self.keyboard = keyboard
            self.letter = self.keyboard.letter
            self.base = self.canvas.create_rectangle(0, 25, 350, 10)
            self.canvas.move(self.base, 100, 450)
            self.stand = self.canvas.create_rectangle(0, 0, 25, 400)
            self.canvas.move(self.stand, 150, 60)
            self.hang = self.canvas.create_rectangle(0, 0, 200, 25)
            self.canvas.move(self.hang, 150, 35)
            self.rope = self.canvas.create_rectangle(0, 0, 1, 50)
            self.canvas.move(self.rope, 260, 60)
            self.partLst = []
            self.boxDict = {}
            self.textDict = {}
            for x in range(len(self.word)):
                box = self.canvas.create_rectangle(0, 0, 20, 20)
                self.canvas.move(box, 220 + 30 * x, 430)
                self.boxDict['box{}'.format(x)] = box
            self.gameOver = None
            self.head = None
            self.body = None
            self.arm1 = None
            self.arm2 = None
            self.leg1 = None
            self.leg2 = None
            self.playAgain = None
            self.winTxt = None
            self.test = 0

        def checkLetter(self):
            if self.word.find(self.letter) == -1:
                if 'head' not in self.partLst:
                    self.head = self.canvas.create_oval(0, 0, 25, 25)
                    self.canvas.move(self.head, 247.5, 110)
                    self.partLst.append('head')
                elif 'body' not in self.partLst:
                    self.body = self.canvas.create_line(0, 0, 0, 40)
                    self.canvas.move(self.body, 260, 135)
                    self.partLst.append('body')
                elif 'arm1' not in self.partLst:
                    self.arm1 = self.canvas.create_line(0, 0, -10, 25)
                    self.canvas.move(self.arm1, 260, 145)
                    self.partLst.append('arm1')
                elif 'arm2' not in self.partLst:
                    self.arm2 = self.canvas.create_line(0, 0, 10, 25)
                    self.canvas.move(self.arm2, 260, 145)
                    self.partLst.append('arm2')
                elif 'leg1' not in self.partLst:
                    self.leg1 = self.canvas.create_line(0, 0, -10, 25)
                    self.canvas.move(self.leg1, 260, 175)
                    self.partLst.append('leg1')
                elif 'leg2' not in self.partLst:
                    self.leg2 = self.canvas.create_line(0, 0, 10, 25)
                    self.canvas.move(self.leg2, 260, 175)
                    self.partLst.append('leg2')
                    self.gameOver = Label(g.root, text='Game\nOver', font='Calibri 72')
                    self.gameOver.grid(column=0, row=0)
                    self.playAgain = Button(g.win, text='Play Again?', command=lambda: self.reset())
                    self.playAgain.grid(column=1, row=1)
                else:
                    self.gameOver = Label(g.root, text='Game\nOver', font='Calibri 72')
                    self.gameOver.grid(column=0, row=0)
                    self.playAgain = Button(g.win, text='Play Again?', command=lambda: self.reset())
                    self.playAgain.grid(column=1, row=1)
            elif self.word.find(self.letter) != -1:
                for x in range(len(self.word)):
                    if self.word.find(self.letter, x, x + 1) != -1:
                        try:
                            if not bool(self.textDict['text{}'.format(x)]):
                                pass
                        except KeyError:
                            boxCoords = self.canvas.coords(self.boxDict['box{}'.format(x)])
                            self.textDict['text{}'.format(x)] = self.canvas.create_text((boxCoords[0] + boxCoords[2]) / 2
                                                                                        , (boxCoords[1] + boxCoords[3]) / 2
                                                                                        , text=self.letter)

        def reset(self):
            global endBool
            g.win.destroy()
            endBool = True

        def getLetter(self):
            self.letter = self.keyboard.letter
            if not endBool:
                if len(self.textDict) == len(self.boxDict):
                    try:
                        if bool(self.canvas.find_withtag(tagOrId=self.winTxt)):
                            pass
                    except _tkinter.TclError:
                        for x in self.textDict:
                            self.canvas.delete(self.textDict[x])
                        self.textDict.clear()
                        for x in self.boxDict:
                            self.canvas.delete(self.boxDict[x])
                        self.boxDict.clear()
                        self.winTxt = Label(g.win, text='You\nWin', font='Calibri 72')
                        self.winTxt.grid(column=0, row=0)
                        self.playAgain = Button(g.win, text='Play Again?', command=lambda: self.reset())
                        self.playAgain.grid(column=1, row=1)
                        print('repeated {} times'.format(self.test))
                        self.test += 1
                        g.win.update()
                        g.win.update_idletasks()
                        time.sleep(5)
    #g.root.find_wit

    g.mainloop()
