import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

while True:
    word = input("Enter a word: ").upper()
    try:
        phonetic_list = [phonetic_dict[letter] for letter in word]
        print(phonetic_list)
        break
    except KeyError:
        print("Sorry only letters in the alphabet please.")
