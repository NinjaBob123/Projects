from random import *
num = randint(0, 1000)
numLst = []
for x in range(10):
  numLst.append(num)
  num = randint(0, 1000)
file = open("numbers.txt", "a")
for x in numLst:
  file.write(str(x))
