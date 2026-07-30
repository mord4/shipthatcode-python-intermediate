def minmax(arr):
    return min(arr), max(arr)

n = int(input())
nums = [int(input()) for _ in range(n)]

a, b = minmax(nums)

print(a)
print(b)