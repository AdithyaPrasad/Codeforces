numbers = input().split()
n = int(numbers[0])
k = int(numbers[1])

if n%2 == 0:
    if k <= (n/2):
        print(2*(k-1)+1)
    else:
        print(2*k-n)
else:
    if k<=((n+1)/2):
        print(2*(k-1)+1)
    else:
        print(2*k-(n+1))