from random import choice


def run_game():
    word: str = choice(["python", "java", "kotlin", "javascript"])

    user_name: str = input("What is your name? ")
    print(f"Welcome to hangman, {user_name}!")

    guessed_letters: str = ""
    tries: int = 3

    while tries > 0:
        blanks: int = 0
        print("Word: ", end="")
        for letter in word:
            if letter in guessed_letters:
                print(letter, end="")
            else:
                print("_", end="")
                blanks += 1

        print()  # Adds a blank line

        if blanks == 0:
            print("Congratulations! You guessed the word!")
            break

        guess: str = input("Guess a letter: ")

        if guess in guessed_letters:
            print(
                f"You already guessed that letter {guess}. Please try with another letter."
            )

        guessed_letters += guess

        if guess not in word:
            tries -= 1
            print(f"That letter is not in the word. You have {tries} tries left.")

            if tries == 0:
                print("Sorry, you lost. The word was: ", word)
                break


if __name__ == "__main__":
    run_game()
