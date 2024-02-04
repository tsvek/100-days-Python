import pandas as pd

game_on = True

while game_on:
    word = input("Enter word: ").lower()
    
    if word == 'exit':
        game_on = False
        break

    df = pd.read_csv("nato_alphabet.csv")
    nato_dict = {row['letter'].lower(): row['code'] for index, row in df.iterrows()}
    answer = [nato_dict[letter] for letter in word]

    print(answer)
    print("Enter 'exit' to exit.")