a = 1
b = 1
sum = 0
while True:
    c = a + b
    if c > 4000000:
        break
    if c % 2 == 0:
        sum += c
    a = b
    b = c

print(sum)
