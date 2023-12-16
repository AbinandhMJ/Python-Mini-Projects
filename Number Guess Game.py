import random

def play_game(max_value, attempts):
    secretnum = random.randint(1, max_value)

    for attempt in range(attempts):
        print(f"\nAttempt {attempt + 1} of {attempts}")
        guess = int(input(f"Guess the number between 1-{max_value}: "))

        if guess == secretnum:
            print(f"Hurray! You guessed it right! The secret number was {secretnum}")
            return True
        elif guess > secretnum:
            print("Your guess is too high. Try again!")
        else:
            print("Your guess is too low. Try again!")

    print(f"\nGame Over! The secret number was {secretnum}. Better luck next time!")
    return False

def main():
    attempts = 3
    score = 0
    max_value = 0

    print("Welcome Player!\nChoose a Level to continue")
    print("1. Easy (Range: 1-20)")
    print("2. Moderate (Range: 1-35)")
    print("3. Hard (Range: 1-100)")
    print("4. Difficult (Range: 1-300)")

    level = int(input("Select a level to start (1-4): "))

    if level == 1:
        max_value = 20
    elif level == 2:
        max_value = 35
    elif level == 3:
        max_value = 100
    elif level == 4:
        max_value = 300
    else:
        print("Invalid level. Exiting the game.")
        return

    print(f"Level {level}: Get ready to guess the secret number in the range 1-{max_value}!")

    if play_game(max_value, attempts):
        score += 10

    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice != "yes":
            print(f"Your Final Score: {score}\nThank you for playing!")
            break
        else:
            max_value += 10
            attempts += 1
            print(f"\nCongratulations! Moving on to the next round with a range of 1-{max_value}.")
            if play_game(max_value, attempts):
                score += 10

if __name__ == "__main__":
    main()
