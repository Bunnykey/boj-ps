num = int(input())
ans = [0] * (1000001)
ans[0] = 0
ans[1] = 0
ans[2] = 1
ans[3] = 1

def finding(N):
  if N >= 4:
    if N % 3 != 0 and N % 2 != 0:
      ans[N] = ans[N-1] + 1
    elif N % 3 == 0 and N % 2 == 0:
      ans[N] = min(ans[N//2], ans[N//3]) + 1
    elif N % 3 == 0 and N % 2 != 0:
      ans[N] = min(ans[N-1],ans[N//3]) + 1
    elif N % 2 == 0 and N % 3 != 0:
      ans[N] = min(ans[N-1],ans[N//2]) + 1
    else:
      ans[N] = ans[N-1] + 1
  return ans[N]

for i in range(num):
  finding(i)

if num == 1:
  print(0)
elif num == 2 or num == 3:
  print(1)
else:
  print(finding(num))