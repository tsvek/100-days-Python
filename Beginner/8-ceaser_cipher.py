
def caesar(task, text, shift):
    answer = ''
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if task == 'encode':
                new_index = position + shift
                if new_index > 25:
                    new_index -= 26
            elif task == 'decode':
                new_index = position - shift
            new_letter = alphabet[new_index]
            answer += new_letter
        else:
            answer += letter
    print(f"The {task}d text is: {answer}")
    

alphabet = [chr(i) for i in range(97, 123)]
restart = 'yes'

while restart == 'yes':  
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(direction, text, shift)
    restart = input("Do you want to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no' and Goodbay=)).\n").lower()
