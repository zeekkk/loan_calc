a = int(input())
b = int(input())
c = int(input())

if c > b:
    print("Excess")
else:
    if c < a:
        print("Deficiency")
    else: print("Normal")
