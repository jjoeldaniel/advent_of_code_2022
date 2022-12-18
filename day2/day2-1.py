global score
score = 0

# Shapes and their respective values
dict = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3,
    'A' : 1,
    'B' : 2,
    'C' : 3,
}

# Compare for matching values
def isTie(opponent_choice, choice):
    if dict[opponent_choice] == dict[choice]:
        return True

def isWin(opponent_choice, choice):

    # Paper vs Rock = Win
    if choice == 'Y' and opponent_choice == 'A':
        return True

    # Scissors vs Paper = Win
    elif choice == 'Z' and opponent_choice == 'B':
        return True

    # Rock vs Scissors = Win
    elif choice == 'X' and opponent_choice == 'C':
        return True
        
    # Else: Loss
    else:
        return False


for line in open("input.txt", "r"):

    # Take both inputs and strip
    shape = line.split(' ')
    shape = [item.strip() for item in shape]

    # Add initial value
    score += dict[shape[1]]

    # Tie
    if isTie(shape[0], shape[1]):
        score += 3
    # Win
    elif isWin(shape[0], shape[1]):
        score += 6
    # Loss
    else:
        score += 0


print(score)
