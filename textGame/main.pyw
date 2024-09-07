from tkinter import *
from time import sleep
from tkinter import Tk
from threading import Thread

breaker = False
broken = False

def printData(data):
    while 1:
        sleep(5)
        print(data.get())

def toggleBreaker():
    global breaker
    breaker = not breaker


def searchLst(obj: dict, val):
    keys = obj.keys()
    for x in keys:
        if x in val:
            keys2 = obj[x].keys()
            for y in keys2:
                return y


class Window:
    def getData(self, change, name):
        if self.entry is not None:
            self.data.set(self.data.get() + self.entry.get() + "\n")
        if self.name is None and name:
            self.name = self.gameName.get()
        if change:
            if self.question.get() == "What is your name?":
                self.question.set("You are a spirit in the void. You can either live as a druid in the forest, or as royalty. You pick. What do you choose?")
                self.label1.update()
                self.entry.delete(0, "end")
            else:
                self.question.set(searchLst(self.actions, self.data.get()))
                self.label1.update()
                self.entry.delete(0, "end")

    def saveGame(self):
        self.getData(False, True)
        with open("gameData.txt", "r") as file1:
            lines = file1.readlines()
            for line1 in lines:
                if self.name in line1:
                    with open("gameData.txt", "a") as file:
                        notWant = []
                        getBool = False
                        lines = file1.readlines()
                        for line in lines:
                            if self.name in line:
                                getBool = True
                            elif getBool:
                                if line == ")\n":
                                    getBool = False
                                elif line != ")\n":
                                    notWant.append(line)
                        with open("saver.txt", "w") as file2:
                            for line2 in lines:
                                if line2 not in notWant:
                                    file2.write(line2)
                            with open("saver.txt", "r") as file3:
                                lines = file3.readlines()
                                open("gameData.txt", "w").close()
                                for line2 in lines:
                                    if self.name in line2:
                                        getBool = True
                                    elif getBool:
                                        if line2 == ")\n":
                                            getBool = False
                                        elif line2 != ")\n":
                                            file.write(self.data.get())
                                    else:
                                        file.write(line2)
                    #self.label1.destroy()
                    self.gameName.destroy()
                    self.submit1.configure(text="Save")
                    self.submit1.grid_forget()
                    self.submit1.grid(column=10, row=10)
                    self.submit2 = Button(self.tk, text="Submit", command=lambda: self.getData(True, False), bg='blue', fg="light blue")
                    self.submit2.grid(column=0, row=3)
                    self.entry = Entry(self.tk, bg="blue")
                    self.entry.grid(column=0, row=2)
                    #self.label2 = Label(self.tk, textvariable=self.data)
                    #self.label2.grid(column=0, row=0)
                    self.tk.update()
                    self.tk.update_idletasks()

            if self.name not in file1:
                file1.close()
                with open("gameData.txt", "a") as file:
                    file.write(f"{self.name} (\n)\n")
                self.gameName.destroy()
                self.submit1.configure(text="Save Game")
                self.submit1.grid(column=10, row=10)
                self.submit2 = Button(self.tk, text="Submit", command=lambda: self.getData(True, False), bg='blue', fg="light blue")
                self.submit2.grid(column=0, row=3)
                self.entry = Entry(self.tk, bg="blue")
                self.entry.grid(column=0, row=2)
                self.question.set("What is your name?")
                self.tk.update()
                self.tk.update_idletasks()

    def newGameStart(self, window: Tk):
        self.start.destroy()
        self.question.set("Game Name")
        self.label1 = Label(window, textvariable=self.question, bg="blue", fg="light blue")
        self.label1.update()
        self.label1.grid(column=0, row=1)
        self.gameName = Entry(window, bg="blue", fg="light blue")
        self.gameName.grid(column=0, row=2)
        self.submit1 = Button(window, bg="blue", text="Submit", command=lambda: self.saveGame(), fg="light blue")
        self.submit1.grid(column=0, row=3)

    def __init__(self):
        self.submit2 = None
        self.entry = None
        self.label2 = None
        self.name = None
        self.tk = Tk()
        self.tk.configure(bg="black")
        self.tk.geometry("500x500")
        self.tk.grid()
        self.title = "Text Based Game: By Hunter Green"
        self.tk.title(self.title)
        self.start = Button(self.tk, text="Start New Game", bg="blue", command=lambda: self.newGameStart(self.tk), fg="light blue")
        self.start.grid(column=0, row=1)
        self.exit = Button(self.tk, text="Exit", bg="red", command=lambda: toggleBreaker())
        self.exit.grid(column=99, row=99)
        self.label1 = None
        self.gameName = None
        self.submit1 = None
        self.data = StringVar()
        self.question = StringVar()
        self.actions = {"forest": {"You are the firstborn of a small family of nomadic druids in the forest. When you turn 13, your parents give you the choise to leave or stay. You believe you are ready to live on your own. Do you leave or stay? \n You have learned how to shoot a bow, & the spell 'fireball'": {"stay": {},
                                                                                                                                                                                                                                                                                                                         "leave": {}}},
                        "royalty": {"You are the last of three children of the King and Queen of the Kingdom of Text. You are neglegted by your parents, as you are third in line for the throne. When you turn thirteen, you have the choise to leave or stay with your abusive parents. Do you leave or stay? \n You learned how to do dishes, the spell laser beam, & how to chop firewood.": {"stay": {},
                                                                                                                                                                                                                                                                                                                                                                                                  "leave": {}}}}
    def mainloop(self):
        while 1:
            if breaker:
                print("You Exited")
                exit(0)
            self.tk.update_idletasks()
            self.tk.update()
            self.getData(False, False)
            if self.label1 is not None:
                self.label1.update()
            sleep(0.01)


w = Window()
f = w.tk
thread = Thread(None, lambda: printData(w.data))
thread.start()

w.mainloop()
