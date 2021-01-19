word = input()
wordList = list(word)
wordList[0] = wordList[0].lower()
for i, w in enumerate(wordList):
    if w.isupper():
        wordList[i] = "_" + wordList[i].lower()
print("".join(wordList))
