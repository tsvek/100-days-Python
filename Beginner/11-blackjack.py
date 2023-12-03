import random
import os

from art import black_logo

def game():
    def new_card(cards):
        '''Choose one card'''
        new_card = random.choice(list(playing_cards))
        cards[new_card] = playing_cards[new_card]
        playing_cards.pop(new_card)

    def lap(cards, player):
        '''Round for hands. Return score'''
        score = sum(list(cards.values()))
        result = score
        if len(list(cards)) == 2 and score == 21:
            if player == True:
                print("You have BlackJack!!!")
            result = 'BlackJack'
        elif player == True and score <= 21:
            print(f'Your cards are {list(cards)}. Current score is {score}.\n')
            more_card = input("Do you want one more card? Type 'yes' or 'no'.\n").lower()
            if more_card in ['+', 'y', 'yes']:
                new_card(cards)
                result = lap(cards, True)      
        elif player == False and score < 17:
            # print(f"Computer has {cards}. Current score {score}")
            new_card(cards)
            # print(f"New computer's card is: {card}")
            result = lap(cards, False)   
        elif score > 21 and 'Ace' in list(cards):
            cards['Ace'] = 1
            score = sum(list(cards.values()))
            if player == False:
                threshold = 17
                player1 = False
            else:
                print("'Ace' costs 1")
                threshold = 21
                player1 = True
            if score > threshold:
                result = score
            else:
                result = lap(cards, player1)
        return result
    
    playing_cards = {'Ace': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
    }
    
    os.system("cls")
    print(black_logo)
    print("Welcome to Blackjack! Let's start.\n")
    players_cards = {}
    computers_cards = {}

    for _ in range(2):
        new_card(players_cards)
        new_card(computers_cards)
    
    first_computers_card = next(iter(computers_cards))
    print(f"    Computer has ['{first_computers_card}','*'].\n")
    player_result = lap(players_cards, True)
    print(f'Your cards are {list(players_cards)}. Current score is {player_result}.\n')
    comp_result = lap(computers_cards, False)
    print(f"Computer has {list( computers_cards)}. Current score is {comp_result}.")
    


    if player_result == comp_result == 'BlackJack' or player_result == comp_result:
        print(f"""    
        Ooooghhh...>_<
        Your cards are {list(players_cards)}.
        Copmuter has {list(computers_cards)}.
        """)
    elif comp_result == 'BlackJack' or player_result > 21 or (comp_result > player_result and comp_result <= 21):
        print(f"""
        You loose! =(
        Your cards are {list(players_cards)}.
        Copmuter has {list(computers_cards)}.
        """)  
    else:
        print(f"""
        You win!!!Congratulation
        Your cards are {list(players_cards)}.
        Copmuter has {list(computers_cards)}.
        """)

    repeat = input("Do you want to play one more time? Type 'yes' or 'no'.\n").lower()
    if repeat in ['+', 'y', 'yes']:
        game()

game()