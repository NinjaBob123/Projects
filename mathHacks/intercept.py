print("Use + for addition, * for multiplication, / for division, x^y for exponets, -- for subtraction, < for square root, and - for negative numbers")
eq = input("What is the equation?: ")
equation = list(eq)
parts = []
part = ''


def isInt(val):
  try:
    int(val)
    return True
  except ValueError:
    return False


for char in equation:
  if char == "+":
    parts.append(part)
    parts.append(char)
    part = ''
  elif char == '-':
    part = ''
    part = part + char
  elif char == '--':
    parts.append(part)
    part = ''
    parts.append(char)
  elif char == '*':
    parts.append(part)
    part = ''
    parts.append(char)
  elif char == '/':
    parts.append(part)
    part = ''
    parts.append(char)
  elif char == '^':
    part = part + char
  elif char == "<":
    parts.append(part)
    part = ''
    parts.append(char)
  elif isInt(char):
    part = part + char
print(parts
