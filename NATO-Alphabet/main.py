import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TO Create a dictionary for the data:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only alphabets are allowed.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()