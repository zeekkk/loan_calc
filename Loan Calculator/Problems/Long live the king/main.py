column = int(input())
row = int(input())

if column in (1, 8) and row in (1, 8):
    print(3)
elif column == 1 or column == 8 or row == 1 or row == 8:
    print(5)
else:
    print(8)
