word = input()
'''
print(ord('a')) #97
print(ord('z')) #122
print(ord('A')) #65
print(ord('Z')) #90
'''
caps = 0
small = 0
for i in word:
    if ord(i) < 95:
        caps += 1
    else:
        small += 1
ans = ""
for letter in word:
    if caps > small:
        if ord(letter) < 95:
            ans += letter
        else:
            ans += chr(ord(letter)-32)
    else:
        if ord(letter) > 95:
            ans += letter
        else:
            ans += chr(ord(letter)+32)
print(ans)