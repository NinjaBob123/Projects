file = open("txt1.txt", "a")
word = "autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism"
while 1:
  try:
    while 1:
      file.write(word)
      word = word + " " + word
  except IOError:
    file.close()
    file = open("txt2.txt", "x")
    file.close()
    file = open("txt2.txt", "a")
