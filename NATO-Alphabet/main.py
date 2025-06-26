import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TO Create a dictionary for the data:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#To Create a list of code words from the word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)