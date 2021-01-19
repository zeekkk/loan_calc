from math import log

a = int(input())
b = int(input())

if b <= 0 or b == 1:
    print(round(log(a), 2))
else:
    print(round(log(a, b), 2))
