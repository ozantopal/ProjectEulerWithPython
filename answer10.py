"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
def is_prime(numb):
    for i in range(2, int((numb ** 0.5)) + 1):
        if numb % i == 0:
            return False
    return True

total = 0

for i in range(2, 2000001):
    if is_prime(i):
        total += i

print(total)
