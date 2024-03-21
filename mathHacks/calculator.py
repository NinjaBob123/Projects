query = input("cone, pyramid, prisim, or interest?: ")
if query == 'cone':
  r = input("radius: ")
  h = input("height: ")
  print(f"V: {(1 / 3) * (3.14 * r ** 2) * h}")
elif query == 'pyramid':
  w = input('width: ')
  l = input('length: ')
  h = input('height: ')
  print(f"V: {(1 / 3)}
