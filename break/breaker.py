from time import sleep
breaker = False
num = 1
file = open(f"txt{1}.txt", "a")
word = "autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism"
for x in range(100):
  try:
    file.write(word)
    word = word + " " + word
  except IOError:
    file.close()
    num += 1
    file = open(f"txt{num}.txt", "x")
    file.close()
    file = open(f"txt{num}.txt", "a")
