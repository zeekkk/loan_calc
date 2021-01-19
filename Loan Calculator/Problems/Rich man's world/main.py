number = int(input())
sums = 7.1 / 100 + 1
counter = 0
while number <= 700000:
    number *= sums
    counter += 1
print(counter)
