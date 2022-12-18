global score
score = 0

# Shapes and their respective values
dict = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
}

# Get shape for choice
def getShape(shape, choice):

    global score

    # Tie
    if choice == 'Y':

        # Requires Rock
        if shape == 'A':
            score += 1
        # Requires Scissors
        if shape == 'C':
            score += 3
        # Requires Paper
        if shape == 'B':
            score += 2

        score += 3
    # Win
    elif choice == 'Z':

        # Requires Paper
        if shape == 'A':
            score += 2
        # Requires Rock
        if shape == 'C':
            score += 1
        # Requires Scissors
        if shape == 'B':
            score += 3

        score += 6
    # Loss
    else:

        # Requires Scissors
        if shape == 'A':
            score += 3
        # Requires Paper
        if shape == 'C':
            score += 2
        # Requires Rock
        if shape == 'B':
            score += 1

        score += 0

f = open("input.txt", "r")
for line in f:

    # Take both inputs and strip
    shape = line.split(' ')
    shape = [item.strip() for item in shape]

    getShape(shape[0], shape[1])

f.close()
print(score)
