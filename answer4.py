"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindromic(n):
    return n == int(str(n)[::-1])

result = 1

for i in range(100, 1000):
    for j in range(i, 1000):
        p = i * j
        if is_palindromic(p) and p > result:
            result = p

print(result)
