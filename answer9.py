"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for i in range(1,1000):
        for j in range(i,1000):
            if i**2+j**2==(1000-i-j)**2:
                print(i*j*(1000-i-j))
