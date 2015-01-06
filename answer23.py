"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
def get_all_divisors(numb):
    divisors = []
    for i in range(1, (numb//2) +1):
        if numb % i == 0:
            divisors.append(i)
    return divisors

def is_abundant(numb):
    divisors = get_all_divisors(numb)
    return sum(divisors[:]) > numb

def get_all_abundant():
    abundants = []
    for i in range(1, 28121):
        if is_abundant(i):
            abundants.append(i)
    return abundants

def is_sum_of_two_abundants(numb, a_list, a_set):
    for i in a_list:
        if i > numb:
            return False
        else:
            if (numb - i) in a_set:
                return True


abundants = get_all_abundant()
abundants_set = set(abundants)

result = 0


for i in range(1, 28124):
    if not is_sum_of_two_abundants(i, abundants, abundants_set):
        result += i

print(result)
