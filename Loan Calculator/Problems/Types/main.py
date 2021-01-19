args = sys.argv
result = []
for i, w in enumerate(args, 1):
    if w.isdigit():
        result.append(int(w))
    if len(result) == 4:
        break
print(result)
