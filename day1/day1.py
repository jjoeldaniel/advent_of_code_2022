f = open("day1\input.txt", "r")
list = []
calories = 0

for line in f:

    if (line == '\n'):
        list.append(calories)
        calories = 0
        continue
    else:
        calories += int(line)

f.close()

list.sort(reverse=True)

print(list[0])
print(list[0] + list[1] + list[2])