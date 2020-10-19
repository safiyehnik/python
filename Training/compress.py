from collections import Counter
word = input()
result = Counter(word)
for x, y in result.items():
    z = str(x) + str(y)
    print(z, end="")