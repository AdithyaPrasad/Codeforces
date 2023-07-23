inputt = input().split(' ')

number = inputt[0]
reps = int(inputt[1])

for i in range(reps):
    if number[-1] == '0':
        number = number[:-1]
    else:
        number = str(int(number)-1)

print(number)
