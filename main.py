n = int(input())
nums = [int(input()) for _ in range(n)]

uniqs = set(nums)

first = nums[0]
first_count = nums.count(first)
second = 0
second_count = 100000

for i in uniqs:
    if nums.count(i) < first_count:
        second = first
        second_count = first_count
        first = i
        first_count = nums.count(i)

    elif nums.count(i) == first_count and i > first:
        second = first
        second_count = first_count
        first = i
        first_count = nums.count(i)

    elif nums.count(i) < second_count:
        second = i
        second_count = nums.count(i)

    elif nums.count(i) == second_count and i > second:
        second = i
        second_count = nums.count(i)


print(second)