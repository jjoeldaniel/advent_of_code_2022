f = open("day1\input.txt", "r")
dict = {}
calories = 0
i = 0

for line in f:

    if (line == '\n'):
        i += 1
        calories = 0
        continue

    calories += int(line)
    dict.update({i : calories})  

f.close()

max = dict[0]
high = 0

for k, v in dict.items():
    if v > max:
        max = v
        high = k

print(dict[high])