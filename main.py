a = input().strip().split()
d = {word: a.count(word) for word in a}

for word, count in d.items():
    print(word, count)