A, B, C = map(int, input().split())

while A != 0 and B != 0 and C != 0:
  if A == 0 and B == 0 and C == 0:
    break
  if A**2 + B**2 == C**2:
    print('right')
  elif B**2 + C**2 == A**2:
    print('right')
  elif C**2 + A**2 == B**2:
    print('right')
  else:
    print('wrong')
  A, B, C = map(int, input().split())