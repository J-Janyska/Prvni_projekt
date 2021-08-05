# Project 1 - Text analyzer
#
# Input texts for analysis

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

line_length = 40
line = "-" * line_length
number_of_texts = len(TEXTS)

registred_users_and_passwords = [
    ("bob", "123"),
    ("ann", "pass123"),
    ("mike", "password123"),
    ("liz", "pass123")
]

stats = {
    "words" : 0,
    "titlecase words" : 0,
    "uppercase words" : 0,
    "lowercase words" : 0,
    "numeric strings" : 0,
    "sum" : 0    }

word_length_occurences = dict()

# Username + password - input & check
print("Enter your username and password.")
user = input("username:")
password = input("password:")

if (user, password) not in registred_users_and_passwords:
    print("Not registred user or incorrect password !")
    exit(1)

# Welcome + text selection prompt
print(line, f"Welcome to the app, {user}.", f"We have {number_of_texts} texts to be analyzed.", line, sep="\n")
user_input = input(f"Enter a number btw. 1 and {number_of_texts} to select:")
print(line)

# User input check
if not user_input.isdigit():
    print("Not an integer value requested !")
    exit(2)

selected_text_index = int(user_input) - 1
if selected_text_index not in range(number_of_texts):
    print(f"We have no such text, a number btw. 1 and {number_of_texts} was expected.")
    exit(3)

# Text analysis
for text_fragment in TEXTS[selected_text_index].split():
    stats["words"] += 1
    word = text_fragment.strip(",.:;")
    word_length_occurences[len(word)] = word_length_occurences.get(len(word), 0) + 1

    if word.istitle():
        stats["titlecase words"] += 1
    elif word.islower():
        stats["lowercase words"] += 1
    elif word.isupper():
        stats["uppercase words"] += 1
    elif word.isdigit():
        stats["numeric strings"] += 1
        stats["sum"] += int(word)

# Print results I - Stats
for stat in stats:
    if stat == "sum":
        print("The sum of all the numbers:", stats[stat])
    elif stat == "words":
        print("There are", stats[stat], "words in the selected text.")
    else:
        print(f"There are {stats[stat]} {stat}.")

# Print results II - Occurences table
occurence_col_width = max(word_length_occurences.values()) + 2
table_headers = ["LEN", "OCCURENCES".center(occurence_col_width), "NR."]

print(line, "|".join(table_headers), line, sep="\n")

for length in sorted(word_length_occurences.keys()):
    occurence = word_length_occurences[length]
    print(f"{length:>{len(table_headers[0])}}|{'*' * occurence:<{len(table_headers[1])}}|{occurence}")

print(line)
