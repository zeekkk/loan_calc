import math
a = int(input())
b = a * math.pi / 180
print(round((math.cos(b) / math.sin(b)), 10))
