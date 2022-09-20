N = int(input())
maxiom = 1
line, A, B = 0, 0, 0

for i in range(2, N):
  if maxiom >= N:
    break
  else:
    maxiom += i
    line = i
div = maxiom - N
A = line - div
B = 1 + div

if N == 1:
  print("1/1")
elif N == 2:
  print("1/2")
elif line %2 == 0:
  print(str(int(A)) + "/" + str(int(B)))
else:
  print(str(int(B)) + "/" + str(int(A)))