import math
M_and_N = input().split()
M = int(M_and_N[0])
N = int(M_and_N[-1])
count = 0
if M % 2 == 1:
    M -= 1
    count = (M/2) * N + math.floor(N/2)
else:
    count = (M/2) * N
print(int(count))