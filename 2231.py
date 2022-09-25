target = int(input())
min_target = abs(target - (len(str(target)) * 9))
 
for i in range(min_target, target):
    temp = sum(map(int, str(i)))
    result = i + temp
    if result == target:
        print(i)
        break
else:
    print(0)