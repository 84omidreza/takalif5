addad = int(input("adda : "))
zakhire = []
for i in range(addad):
  zakhire.append([])
  zakhire[i].append(1)
  for x in range(1, i):
    zakhire[i].append(zakhire[i - 1][x - 1] + zakhire[i - 1][x])
  if(addad != 0):
    zakhire[i].append(1)
for i in range(addad):
  print(" " * (addad - i))
  for x in range(0, i + 1):
    print('{0:6}'.format(zakhire[i][x]), end = " ", sep = " ")
  print()