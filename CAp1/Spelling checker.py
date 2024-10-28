import re

dzongkha_dictionary = set() 

with open('dzongkha.txt', 'r', encoding='utf-8') as dict_file:
    for line in dict_file:
        dzongkha_dictionary.add(line.strip())

with open('341.txt', 'r', encoding='utf-8') as passage_file:
    passage = passage_file.readlines()

misspelled_words = []

for line_num, line in enumerate(passage, 1):
    words = re.findall(r'\b\S+\b', line)
    for pos, word in enumerate(words):
if word not in dzongkha_dictionary:
            misspelled_words.append((word, line_num, pos + 1))

if misspelled_words:
    print("Misspelled words found:")
    for word, line_num, pos in misspelled_words:
        print(f"'{word}' at line {line_num}, position {pos}")
else:
    print("No misspelled words found.")