from threading import Thread
from time import sleep
breaker = False


def end():
  global breaker
  sleep(20)
  breaker = True


file = open("txt1.txt", "a")
ender = Thread(target=end, args=None, daemon=True)
ender.start()
word = "autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism"
while 1:
  try:
    while 1:
      if breaker:
        exit(0)
      file.write(word)
      word = word + " " + word
  except IOError:
    file.close()
    file = open("txt2.txt", "x")
    file.close()
    file = open("txt2.txt", "a")
