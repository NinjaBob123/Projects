file = open("txt1.txt")
word = "autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism autism"
while 1:
  try:
    while 1:
      file.write(word)
  except IOError:
    pass
