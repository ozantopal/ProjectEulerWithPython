"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def sum_of_evenly_divisors(numb):
    divisors_sum = 0
    for i in range(1, (numb//2) + 1):
        if numb%i == 0:
            divisors_sum += i
    return divisors_sum

def is_amicable(numb):
    other = sum_of_evenly_divisors(numb)
    if numb != other:
        if sum_of_evenly_divisors(other) == numb:
            return True
        else:
            return False
    else:
        return False

result = 0
for i in range(2, 10000):
    if is_amicable(i):
        result += i

print(result)
