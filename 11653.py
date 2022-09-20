N = int(input())
primeList = []

def isPrime(n):
    testn = int(n)
    if testn == 1:
        return False
    for i in range(2,int(testn**0.5)+1):
        if testn % i == 0:
            return False
    return True

for i in range(1, N+1):
  if isPrime(i) == True:
    primeList.append(i)

k = 0

#print(primeList)

for i in range(20):
  if N % primeList[k] == 0:
    N /= primeList[k]
    print(primeList[k])
  else:
    k += 1