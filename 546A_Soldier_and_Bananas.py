values = input()
values = values.split()
values = [int(j) for j in values]
k = values[0]
n = values[1]
w = values[2]
cost = 0
for i in range(1,w+1):
    cost += i*k
if (cost-n) < 0:
    print(0)
else:
    print(cost-n)