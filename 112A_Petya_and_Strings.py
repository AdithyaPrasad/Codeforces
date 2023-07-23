first = input().lower()
second = input().lower()
for i in range(len(first)):
    if ord(first[i]) < ord(second[i]):
        print('-1')
        break
    elif ord(first[i]) > ord(second[i]):
        print('1')
        break
    else:
        continue
else:
    print('0')