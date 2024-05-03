from random import randint

lower_num, higher_num = 1, 10
random_num: int = randint(lower_num, higher_num)

print(
    f"Welcome to the number guessing game! Guess a number between {lower_num} and {higher_num}."
)


for counter in range(3):
    try:
        user_guess = int(input("Enter your guess: "))
        if user_guess == random_num:
            print(f"You guessed the correct number in {counter + 1} guesses!")
            break
        print(
            "Your guess is too low."
            if user_guess < random_num
            else "Your guess is too high."
        )
    except ValueError:
        print("Invalid input. Please enter a number.")
else:
    print(
        f"You've reached the maximum number of guesses. The correct number was {random_num}."
    )
