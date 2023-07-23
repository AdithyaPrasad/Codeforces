n = input()
stones = list(input())
count = 0
while len(stones) > 1:
    if stones [0] == stones [1]:
        count += 1
    stones = stones[1:]
print(count)