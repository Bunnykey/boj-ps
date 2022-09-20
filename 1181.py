N = int(input())
strlist = []

for _ in range(N):
  strlist.append(input())

anslist = list(set(strlist))
anslist.sort()

reslist = []
lenlist = []

for k in range(len(anslist)):
  lenlist.append(len(anslist[k]))

for i in range(1,max(lenlist)+1):
  for j in range(len(anslist)):
    if len(anslist[j]) == i:
      reslist.append(anslist[j])
      continue

for i in range(len(reslist)):
  print(reslist[i])