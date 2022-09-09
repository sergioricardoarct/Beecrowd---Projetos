a, b = input().split()
while a != '0' and b != '0':
  new = b.replace(a, "")
  if new == '':
    new = 0
  print(int(new))
  a, b = input().split()