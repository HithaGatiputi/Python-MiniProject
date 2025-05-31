import refer
print(refer.logo_c)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = " "
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
        else :
            end_text += char
    print(f"The {cipher_direction} text is {end_text}")

play_again = True
while play_again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    new_shift = shift % 26
    caesar(start_text=text, shift_amount=new_shift, cipher_direction=direction)
    play = input("Type 'yes' if you wany to go again. Otherwise type 'no'.\n")
    if play == "no":
        play_agin = False
        print("Goodbye")
        break


