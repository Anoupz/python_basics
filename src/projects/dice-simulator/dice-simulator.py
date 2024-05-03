import random


def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError("The amount of dice must be greater than 0.")
    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls


def main():
    print("Welcome to the dice simulator!")
    while True:
        try:
            amount_of_dice: int = int(
                input("Enter the amount of dice to roll: ")
            )
            dice_rolls: list[int] = roll_dice(amount_of_dice)
            print(*dice_rolls, sep=", ")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        finally:
            play_again: str = input("Would you like to roll again? (yes/no): ")
            if play_again.lower() != "yes":
                print("Goodbye!")
                break


if __name__ == "__main__":
    main()
