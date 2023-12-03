import random
import os

from art import guess_logo


def check_guess(guess, number):
    if guess == number:
        return "win"
        # return -1
    elif guess > number:
        return "Too hight."
        # return attempts - 1
    else:
        return "Too low."
        # return attempts - 1


def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'.\n").lower()
    if difficulty == 'easy':
        return 10
    else:
        return 5


def game():
    os.system("cls")
    print(guess_logo)
    print("Welcome! Let's try to guess the number=)")
    number = random.randrange(1, 100)
    print(f"Spoiler: correct number is {number}.")

    attempts = choose_difficulty()
    guess = 0
    while guess != number:
        print(f"You have {attempts} attempts before lose.")
        guess = int(input("Make a guess: "))
        result = check_guess(guess, number)
        if result == "win":
            print("    Congratulations! You guess the number!")
            break
        print(result)
        attempts -= 1
        if attempts == 0:
            print(f"You have {attempts} attempts.\n    You lose!!!")
            return
        else:
            print("Guess again.")


game()
