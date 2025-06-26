import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TO Create a dictionary for the data:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)