"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
def get_largest_prime_factor(n):
    f = 1

    while n > 1:
        f += 1
        while n % f == 0:
            n /= f

    return f


n = 600851475143
print(get_largest_prime_factor(n))
