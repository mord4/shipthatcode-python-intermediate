from collections import defaultdict

n = int(input())
a = [input().strip().split() for _ in range(4)]

d = defaultdict(list)
for key, value in a:
    d[value].append(key)

for k, v in d.items():
    print(k + ":", ", ".join(v))