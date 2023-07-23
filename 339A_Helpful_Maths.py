s = [int(i) for i in (input().split('+'))]
s.sort()
ans= []
for j in s:
    ans.append(j)
    ans.append('+')
ans.pop()
ans = [str(k) for k in ans]
ans = ''.join(ans)
print(ans)