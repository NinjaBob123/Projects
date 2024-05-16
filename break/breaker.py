from pynput.keyboard import Listener, Key
breaker = False


def end(key):
  global breaker
  if key == Key.esc:
    breaker = True


file = open("txt1.txt", "a")
keyLstn = Listener(onpress=end)
word = "autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism"
while 1:
  if breaker:
    break
  try:
    while 1:
      if breaker:
        break
      file.write(word)
      word = word + " " + word
  except IOError:
    file.close()
    file = open("txt2.txt", "x")
    file.close()
    file = open("txt2.txt", "a")
