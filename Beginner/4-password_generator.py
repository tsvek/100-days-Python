import random

alhpabet = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
numbers_list = [chr(i) for i in range(48, 58)]
symbols_list = ["~", "!", "@", "#", "$", "%", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", ":", ";", "<", ">", "?"]
print("Welcome to my Password Generator")

password = ""
letters = int(input("How many letter do you want? "))
symbols = int(input("How many symbols? "))
numbers = int(input("And what about numbers? "))

for char in range(letters):
    password += random.choice(alhpabet)
for char in range(symbols):
    password += random.choice(symbols_list)
for char in range(numbers):
    password += random.choice(numbers_list)

p_shuffle = random.sample(password, len(password))

print(''.join(p_shuffle))