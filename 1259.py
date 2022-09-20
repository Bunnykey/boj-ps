s = input()
while s != "0":
  if s == ''.join(list(reversed(s))):
    print("yes")
  else:
    print("no")
  s = input()