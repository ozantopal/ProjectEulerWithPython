"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

result = 0

for a in range(1, 100):
	for b in range(1, 100):
		numb = a ** b
		temp = sum([int(i) for i in str(numb)])		
		if temp > result:
			result = temp

print(result)
