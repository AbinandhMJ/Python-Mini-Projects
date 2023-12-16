import random

attempts = 3
score = 0
easy = 20
moderate = 35
hard = 100
difficult = 300

Levels = """
1, Easy
2, Moderate
3, Hard
4, Difficult
"""


max_value = 0
print(f"Welcome Player!\n Choose a Level to continue \n"
      f"Levels: {Levels}")
Level = int(input("Select a level to start!: "))
if Level == 1:
    max_value = easy
    print("Level 1: Easy")
elif Level == 2:
    max_value = moderate
    print("Level 2: Moderate")
elif Level == 3:
    print("Level 3: Hard")
    max_value = hard
elif Level == 4:
    print("Level 4: Difficult")
    max_value = difficult
else:
    print("Select a Level to Continue!...")

secretnum = random.randint(1, max_value)

for attempt in range(attempts):
    print(f"LEVEL: {Level} ")
    print("I've Got a Secret Number! Guess it Now!...")
    print(secretnum)
    guess = int(input(f"Guess the number between 1-{max_value}: "))

    if guess == secretnum:
        score += (attempt + attempts) * 10
        print(f"Hurray! You Won\nYour Score: {score}")
        choice = input("Do you want to continue? (Yes/No): ")
        if choice.lower() == "yes":
            max_value += 10
            print(f"Congratulations! Moving on to the next round with a range of 1-{max_value}.")
            continue
        else:
            print(f"Your Score: {score}\n Thankyou for Playing")
            break
    elif guess > secretnum:
        print("Your guess is too high\n Try Again!")
    elif guess < secretnum:
        print("Your guess is too low\n Try Again!")

if guess != secretnum:
    print(f"Game Over!..., Your Score: {score}\n Thankyou for playing")
#
# for attempt in range(attempts):
#
#     guess = int(input("Guess the number between 1-20: "))
#     if guess == secretnum:
#         score += (attempt + attempts) * 10
#         print(f"You Won! your score is {score}")
#         break
#     elif guess > secretnum:
#         print("Your guess is too high")
#     elif guess < secretnum:
#         print("Your guess is too low")
#
# if guess != secretnum:
#         print(f"Game Over!!! number is {secretnum}")



# import random
#
# num = random.randint(1, 20)
#
# max_attempts = 3
# attempt = 0
#
# while attempt < max_attempts:
#     guess = int(input("Guess the number between 1-20: "))
#     attempt += 1
#
#     if guess == num:
#         print("You Won!")
#         break
#     elif guess > num:
#         print("Your guess is higher!")
#     else:
#         print("Your guess is lower!")
#
# if attempt == max_attempts and guess != num:
#     print(f"Sorry, you've run out of attempts. The correct number was {num}.")
