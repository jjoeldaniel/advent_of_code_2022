global sum
sum = 0

def getPriority(char):
    if ord(char) <= 122 and ord(char) >= 97:
        return ord(char) - 96
    else:
        return ord(char) - 38

for line in open("input.txt", "r"):
    first = line[slice(0, len(line)//2)]
    second = line[slice(len(line)//2, len(line))]
    
    i = 0

    for char in first:
        if char in second:
            sum += getPriority(char)
            break

print(sum)