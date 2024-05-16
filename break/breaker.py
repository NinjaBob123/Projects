from threading import Thread
from time import sleep
breaker = False
num = 1


def end():
  global breaker
  sleep(20)
  breaker = True


file = open(f"txt{1}.txt", "a")
ender = Thread(target=end, args=None, daemon=True)
ender.start()
word = "autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism"
while 1:
  try:
    while 1:
      if breaker:
        file.close()
        exit(0)
      file.write(word)
      word = word + " " + word
  except IOError:
    file.close()
    num += 1
    file = open(f"txt{num}.txt", "x")
    file.close()
    file = open(f"txt{num}.txt", "a")
