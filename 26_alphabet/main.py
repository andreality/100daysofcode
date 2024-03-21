import pandas as pd

alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")

# Loop through rows of a data frame
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def convert_word():
    word = input("Enter a word, any word will do.")
    try:
        nato_list = [alphabet_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Please only enter letters of the alphabet; try again.")
        convert_word()
    else:
        print(nato_list)

convert_word()