Matrix = []
row = 0
column = 0
for k in range(5):
    line = input().split()
    if '1' in line:
        row = k
        column = line.index('1')
    Matrix.append(line)
answer = abs(row-2) + abs(column-2)
print(answer)