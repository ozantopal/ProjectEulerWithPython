"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial

numbers = []
for numb in range(3, 9999999):
	temp = 0
	for i in str(numb):
		temp += factorial(int(i))
	if temp == numb:
		numbers.append(numb)

result = 0
for i in numbers:
	result += i

print(result)
