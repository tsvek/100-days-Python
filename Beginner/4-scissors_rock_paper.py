import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

rps = [rock, paper, scissors]
computer_choice = random.choice(rps)
user_choice = int(input('What do you choose? \n0 - rock \n1 - paper \n2-scissors \n'))
if user_choice not in range(0,3):
  print("You must to choose only from 0 or 1 or 2!!")
else:
  user_choice = rps[user_choice]
  print_choices = f'''
    You choice is: \n{user_choice}
    Computer choice is: \n{computer_choice}
    '''
  if user_choice == computer_choice:
    print(print_choices + "It\'s draw. Try again!")
  elif computer_choice == rock and user_choice == paper:
      print(print_choices + "You win! Congratulations!!!")
  elif computer_choice == paper and user_choice == scissors:
      print(print_choices + "You win! Congratulations!!!")
  elif computer_choice == scissors and user_choice == rock:
      print(print_choices + "You win! Congratulations!!!")
  else:
      print(print_choices + "You loose!")

