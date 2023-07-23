n = int(input())
a = [int(i) for i in list(input().split(' '))]
count = 0
coins = 0
for k in range(n):
    count += 1
    maximum = max(a)
    coins += max(a)
    a.remove(maximum)
    sum = 0
    for j in a:
        sum += j
    if coins > sum:
        print(count)
        break
