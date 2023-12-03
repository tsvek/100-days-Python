import os

from art import hilo_logo, vs
from hilo_data import data
from random import choice


def rand_user():
    """Return random user from dataset."""
    return choice(data)


def info_print(user):
    """Return string with user info: name, description, country."""
    return f"{user['name']} is a {user['description']} from {user['country']}"


def compare_users(guess, user1, user2):
    """Compare users folowwers, then with guess. Return True if guess correct and False if not."""
    if user1['follower_count'] > user2['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'

print(hilo_logo)
score = 0
fact1 = rand_user()

while True:    
    fact2 = rand_user()
    if fact1 == fact2:
        fact2 = rand_user()

    print("Compare this('A'): " + info_print(fact1))
    print(vs)
    print("With this('B'): " + info_print(fact2))
    player_guess = input("Who has more followers? Type 'A' or 'B'.\n").lower()
    
    os.system("cls")
    
    print(hilo_logo)
    result = compare_users(player_guess , fact1, fact2)
    if result:
        score += 1
        fact1 = fact2
        print(f"Yep. Current score: {score}")
    else:
        print(f"Nope. Final score: {score}")
        break
 
