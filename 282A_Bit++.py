total  = int(input())
count = 0
for i in range(total):
    program = input()
    if '+' in program:
        count += 1
    else:
        count -= 1
print(count)