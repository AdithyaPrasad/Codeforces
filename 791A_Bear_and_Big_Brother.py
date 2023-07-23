a_and_b = input()
a_and_b = a_and_b.split()
a = int(a_and_b[0])
b = int(a_and_b[-1])
year = 0
while a <= b:
    a = 3*a
    b = 2*b
    year += 1
print(year)