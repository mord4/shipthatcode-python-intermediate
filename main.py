def is_palindrome(line):
    return line == line[::-1]


a = "".join(input().strip().split()).lower()

print("yes" if is_palindrome(a) else "no")