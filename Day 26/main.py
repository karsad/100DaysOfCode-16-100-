# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {value.letter:value.code for key, value in alphabet_data.iterrows()}
print(alphabet_dict)

user_input = "0"
while user_input.lower() != 'exit':
    user_input = input("Enter a word: ")
    output = [alphabet_dict[letter.upper()] for letter in user_input if letter.upper() in alphabet_dict]
    print(output)