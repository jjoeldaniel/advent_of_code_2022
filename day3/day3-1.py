global sum
sum = 0

def getPriority(char):
    if ord(char) <= 122 and ord(char) >= 97:
        return ord(char) - 96
    else:
        return ord(char) - 38

f = open("input.txt", "r")
for line in f:
    first = line[slice(0, len(line)//2)]
    second = line[slice(len(line)//2, len(line))]
    
    i = 0

    for char in first:
        if char in second:
            sum += getPriority(char)
            break

f.close()
print(sum)