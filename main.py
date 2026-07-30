n = int(input())
print(sorted(list(set([int(input()) for _ in range(n)])))[-2])
