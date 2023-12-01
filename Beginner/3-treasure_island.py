top = """
 _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|
 
 """
game = True

while game:
    print(top)

    print("""Welcome to  Treasure Island.
        Your mission is to find the treasure.
        """)
    cross = input("You are at cross road. Where do you want to go? Type 'left' or 'right': ")
    if cross != "left":
        print("You fall into a hole. \n GAME OVER!")
        game = False
        break
    lake = input("You come to a lake. There is an island in the middle. Type 'wait' to wait the boat, 'swim' to swim across. ")
    if lake != "wait":
        print("You've been attacked by trout. \n GAME OVER!")
        game = False
        break
    door = input("You arrive at the island. There is a house with 3 doors: red, gree, blue. Which one you will you choose? ")
    if door == "green":
        print("Congratulations!! You win one pucik!")
        game = False
    else:
        print("Please choose the way of your death by yourself. \n Anyway GAME OVER!")
        game = False