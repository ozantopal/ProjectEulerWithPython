"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def is_prime(numb):
    for i in range(2, int((numb ** 0.5)) + 1):
        if numb % i == 0:
            return False
    return True

def next_prime(previous):
    next = previous
    while True:
        next += 1
        if is_prime(next):
            break
    return next

prime = 1
for i in range(1, 10002):
    prime = next_prime(prime)

print(prime)
