import re

i = 0

for line in open("input.txt", "r"):
    numbers = re.split(r'-|,', line)
    numbers = [item.strip() for item in numbers]

    x = set(range(int(numbers[0]), int(numbers[1])))
    y = set(range(int(numbers[2]), int(numbers[3])))

    # TODO: fix
    if x.issubset(y) or y.issubset(x):
        i += 1

print(i)