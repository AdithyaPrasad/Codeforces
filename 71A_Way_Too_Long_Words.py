length = int(input())
for i in range(length):
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        print(word[0]+str(len(word[1:-1]))+word[-1])