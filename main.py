alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# take a string and shift the letters forward according to the specified shift value
def caesar_cipher(mode, text, shift):
    new_text = ""
    for char in text:
        if not char.isalpha():
            new_text += char
        else:
            for pos in range(len(alphabet)):
                if alphabet[pos] == char:
                    if mode == "encode":
                        new_position = (pos + shift) % len(alphabet)
                    else:
                        new_position = (pos - shift) % len(alphabet)

                    new_text += alphabet[new_position]
    return new_text

# get input from user
direction = ""
while direction != "encode" and direction != "decode":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

text = input("Type your message:\n").lower()
shift = -1
while shift < 0:
    shift = int(input("Type the shift number:\n"))
    if shift < 0:
        print("Please enter a positive shift value.")

print(f"Here's the result: {caesar_cipher(direction, text, shift)}")

