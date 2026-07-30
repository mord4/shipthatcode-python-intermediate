a = set(input().strip().split())
b = set(input().strip().split())

print(" ".join(sorted(list(a & b))))