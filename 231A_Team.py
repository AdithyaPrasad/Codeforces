problems = int(input())
count = 0
for i in range(problems):
    solns = list(input())
    counting = 0
    for j in solns:
        if j == '1':
            counting += 1
    if counting >= 2:
        count +=1
print(count)