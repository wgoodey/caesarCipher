alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# take a string and shift the letters forward according to the specified shift value
def encrypt(text, shift):
    cipher_text = ""
    for char in text:
        if not char.isalpha():
            cipher_text += char
        else:
            for pos in range(len(alphabet)):
                if char == alphabet[pos]:
                    if pos + shift > len(alphabet) - 1:
                        cipher_text += alphabet[pos + shift - len(alphabet)]
                    else:
                        cipher_text += alphabet[pos + shift]
                    break
    return cipher_text


# take a string and shift the letters backward according to the specified shift value
def decrypt(text, shift):
    plain_text = ""
    for char in text:
        if not char.isalpha():
            plain_text += char
        else:
            for pos in range(len(alphabet)):
                if char == alphabet[pos]:
                    if pos - shift < 0:
                        plain_text += alphabet[pos - shift + len(alphabet)]
                    else:
                        plain_text += alphabet[pos - shift]
                    break
    return plain_text


# get input from user
direction = ""
while direction != "encode" and direction != "decode":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


if direction == "encode":
    print(f"Here's the encoded result: {encrypt(text, shift)}")
elif direction == "decode":
    print(f"Here's the decoded result: {decrypt(text, shift)}")
else:
    print("Sorry, invalid input.")
