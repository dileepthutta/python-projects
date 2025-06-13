import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)


def caesar(original_text, shift_amount, encode_or_decode):
            if encode_or_decode == "decode":
                shift_amount *= -1
            output_text = ""
            for letter in original_text:
                if letter not in alphabet:
                    output_text+=letter
                else:
                    shifted_position = alphabet.index(letter) + shift_amount
                    shifted_position %= len(alphabet)
                    output_text += alphabet[shifted_position]
            print(f"Here is the {encode_or_decode}d result: {output_text}")



should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction in ['encode', 'decode']:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
        yes_or_no = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
        if yes_or_no=="no":
            should_continue=False
            print("GoodBye!")
        # else:
        #     print("Enter a valid input or type 'no' to exit!\n")
    else:
        quit("Sorry you have entered a in-valid input")

