import pandas


# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alpha_dict = {row.letter: row.code for index, row in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

user_input = input()
phonetic_code = [phonetic_alpha_dict[char.upper()] for char in user_input if char.isalpha()]
print(phonetic_code)










