import re

file = open("regex_sum_2248121.txt")

numbers = []

for line in file:
    num = re.findall('[0-9]+', line)
    
    for n in num:
        numbers.append(int(n))

print(sum(numbers))