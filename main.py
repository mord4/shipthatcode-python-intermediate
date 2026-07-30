def average(*nums):
    return sum(nums) / len(nums)


n = int(input())
nums = [float(input()) for _ in range(n)]
# Call average(*nums) and print rounded to 2 decimal places
print(f"{average(*nums):.2f}")
