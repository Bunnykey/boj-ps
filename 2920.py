res = list(map(int, input().split()))

org = res
asc = list(sorted(res))
rev = list(reversed(asc))

if org == asc:
  print("ascending")
elif org == rev:
  print("descending")
else:
  print("mixed")