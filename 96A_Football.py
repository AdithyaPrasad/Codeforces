line = input()

current = line[0]
count = 1
for i in line[1:]:
    if current == i:
        count += 1
        current = i
    else:
        current = i
        count = 1
    if count == 7:
        print("YES")
        break
if count < 7:
    print("NO")