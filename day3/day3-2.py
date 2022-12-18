global sum
sum = 0

global i
i = 0

global list
list = []

def getPriority(char):
    if ord(char) <= 122 and ord(char) >= 97:
        return ord(char) - 96
    else:
        return ord(char) - 38

def getBadge(list):

    for char in list[0]:
        if char in list[1] and char in list[2]:
            return char

f = open("input.txt", "r")
for line in f:

    list.append(line)
    i += 1

    if i == 3:
        i = 0
        sum += getPriority(getBadge(list))
        list = []

f.close()
print(sum)