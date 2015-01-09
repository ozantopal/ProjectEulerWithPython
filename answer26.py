"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
from decimal import *
 
def find_fraction(i):
    getcontext().prec = 1500
    x = Decimal(1) / Decimal(i)
    return x
 
def find_period(numb):
    L = (str(numb))
    length = len(L)
    l1, l2, l3 = 0, 0, 0
    if L[2:3] != '0':
        index = L[2:6]
        l1 = 1
    elif L[2:3] == '0' and L[3:4] != '0':
        index = L[3:7]
        l2 = 1
    elif L[2:3] == '0' and L[3:4] == '0':
        index = L[4:8]
        l3 = 1
    max_period = 0
    for v in range(3, length):
        if l1 == 1:
            indexi = L[v:(v + 4)]
        elif l2 == 1:
            indexi = L[(v + 1):(v + 5)]
        elif l3 == 1:
            indexi = L[(v + 2):(v + 6)]
        if index == indexi:
            max_period = v
            break
    return max_period

place_holder = 0
for i in range(1, 1000):
    x = find_fraction(i)
    y = find_period(x)
    if y > place_holder:
        place_holder = y
        result = i

print(result)
