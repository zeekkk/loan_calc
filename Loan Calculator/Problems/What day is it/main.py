hours = int(input())

TIME = 10

if TIME + hours < 0:
    print("Monday")
elif TIME + hours >= 24:
    print("Wednesday")
else:
    print("Tuesday")
