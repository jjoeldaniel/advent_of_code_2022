list = []
calories = 0

for line in open("input.txt", "r"):

    if (line == '\n'):
        list.append(calories)
        calories = 0
    else:
        calories += int(line)

list.sort(reverse=True)

print(list[0])
print(list[0] + list[1] + list[2])