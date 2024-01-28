logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        idx = alphabet.index(letter)
        shifted_idx = (idx + shift_amount) % 26
        new_letter = alphabet[shifted_idx]
        cipher_text += new_letter
    return cipher_text

def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        idx = alphabet.index(letter)
        shifted_idx = (idx - shift_amount) % 26
        new_letter = alphabet[shifted_idx]
        cipher_text += new_letter
    return cipher_text

def caesar(direction_type, plain_text, shift_amount):
    if direction_type not in ["encode", "decode"]:
        print("Direction type must be one of: encode, decode.")
        return
    cipher_text = ""
    for letter in plain_text:
        if letter not in alphabet:
            cipher_text += letter
            continue
        idx = alphabet.index(letter)
        if direction_type == "decode":
            shifted_idx = (idx - shift_amount) % 26
        else:
            shifted_idx = (idx + shift_amount) % 26
        new_letter = alphabet[shifted_idx]
        cipher_text += new_letter
    print(f"The {direction_type}d text is {cipher_text}.")


go_again = True
while go_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction_type=direction, plain_text=text, shift_amount=shift)
    go_again_text = input("Would you like to go again Y / N?")
    if go_again_text.upper() == "N":
        go_again = False

