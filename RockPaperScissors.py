import random

def play():
    while True:
        user = input("R for Rock, P for Paper, S for Scissors \nEnter your choice to Continue: ").lower()

        if user in ['r', 'p', 's']:
            break
        else:
            print("Invalid entry. Please enter a valid input (R, P, or S).")

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "Ouch!..it's a tie!"

    if is_win(user, computer):
        return "You Won"

    return "You Lost"

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

print(play())
