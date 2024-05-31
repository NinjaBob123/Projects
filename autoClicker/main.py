from pynput.mouse import Controller, Button
from pynput.keyboard import Listener
from time import sleep, time
from threading import Thread
num = 5
breaker = False
cps = input("What cps do you want to click at? Recommend under 10000: ")
tm = input("How long do you want to click for in seconds?: ")
while num > 0:
    print(f"Clicking in {num}")
    num -= 1
    sleep(1)
cont = Controller()


def stop(key):
    global breaker
    if key == '`':
        breaker = not breaker


def stoper():
    while 1:
        stopd = input("Toggle?: ")
        if stopd != None:
            stop('`')


listn = Listener(on_press=stop)
stoper = Thread(target=stoper)
stoper.start()
listn.start()
start = time()
while 1:
    if breaker:
        pass
    elif not breaker:
        if float(cps) < 10000:
            cont.press(Button.left)
            cont.release(Button.left)
            sleep(1/ (int(cps) + 25))
        elif float(cps) >= 10000:
            cont.press(Button.left)
            cont.release(Button.left)
    if tm != "":
        new = time()
        if new - start >= float(tm):
            break
