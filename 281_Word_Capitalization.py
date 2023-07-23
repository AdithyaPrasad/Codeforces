line = list(input())
value = ord(line[0])
if value < 91:
    pass
else:
    line[0] = chr(value-32)
print(''.join(line))