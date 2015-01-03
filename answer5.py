"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

prime_factors = (2, 3, 5, 7, 11, 13, 17, 19)
value = 1
for prime_factor in prime_factors:
    for x in range(1, 6):
        if prime_factor**x > 20:
            break
    value = value * (prime_factor**(x-1))

print(value)
