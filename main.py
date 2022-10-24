import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# take a string and shift the letters forward according to the specified shift value
def caesar_cipher(mode, text, shift):
    output = ""
    if mode == "decode":
        shift *= -1
    shift %= len(alphabet)
    for char in text:
        if not char.isalpha():
            output += char
        else:
            for pos in range(len(alphabet)):
                if alphabet[pos] == char:
                    new_position = (pos + shift)
                    output += alphabet[new_position]
    return output


print(art.logo)

end = False

while not end:

    # get input from user
    direction = ""
    while direction != "encode" and direction != "decode":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()
    shift = 0
    while shift == 0:
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("Please enter an integer for the shift value.")

    print(f"Here's the result: {caesar_cipher(direction, text, shift)}")

    again = input('\n\nDo you want to run again? Type "yes".\n').lower()
    if again != "yes":
        end = True
    else:
        print("Goodbye")
