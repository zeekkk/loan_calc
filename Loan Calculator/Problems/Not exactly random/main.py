# place `import` statement at top of the program
from random import seed
from random import randint

# don't modify this code or variable `n` may not be available
n = int(input())

seed(n, 2)
print(randint(-100, 100))

# put your code here
