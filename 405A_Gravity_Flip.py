n = input()
a = input().split()
a = [int(i) for i in a]
value = False
while value == False:
    value == True
    for i in range(len(a)-1):
        print(a,i)
        if a[i] > a[i+1]:
            value = False
            diff = (a[i]-a[i+1])
            a[i] -= diff
            a[i+1] += diff
print(a)