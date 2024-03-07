from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):

    cipher=""
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position=position+shift
            new_text= alphabet[new_position]
            cipher+=new_text
        else:
            cipher+=i
    print(cipher)


def decrypt(cipher,shift):
    plain_text=""
    for i in cipher:
        if i in alphabet:
            position = alphabet.index(i)
            new_position=position-shift
            new_text = alphabet[new_position]
            plain_text+=new_text
        else:
            plain_text+=i
    print(plain_text)
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift %26

    if direction=="encode":
        encrypt(text,shift)
    elif direction=="decode":
        decrypt(cipher=text,shift=shift)
    else:
        print("Enter a valid type")
    res = input("Enter Yes to continue again, No to exit: ").lower()
    if res=="no":
        should_continue=False
        print("Thank You!")
