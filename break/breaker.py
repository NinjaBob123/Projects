from time import sleep
breaker = False
num = 1
word = "autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism"
for x in range(100):
  try:
    print(word)
    word = word + " " + word
  except IOError:
    raise Error("File out of space, go to next file")
