"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

data = open("names.txt").read()
names = map(lambda name: name.strip("\""), data.split(","))
sorted_names = sorted(names)

def value_of_name(name):
    result = 0
    for letter in name:
        result += ord(letter) - ord("A") + 1
    return result


result = 0
for i in range(0, len(sorted_names)):
    result += value_of_name(sorted_names[i]) * (i + 1)

print(result)
