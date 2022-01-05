student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in nato_csv.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def get_name():
    try:
        name = input("What is your name? :")
        nato = [new_dict[l.upper()] for l in name]
        return nato
    except KeyError or TypeError:
        print("Sorry, only letters in the alphabet please")
        get_name()


list_nato = get_name()
print(list_nato)
