x = int(input())
ans = 1 + int(x/5)
if x%5 == 0:
    ans -= 1
print(ans)