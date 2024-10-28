import re

# A sample list of correct Dzongkha words (you'll want a more comprehensive list for real use)
dzongkha_words = {'བོད་', 'མི་', 'དབུ་', 'འབུ་', 'གོ་'}

# Read the content of the file
with open('dzongkha_only.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Split the text into words (assuming spaces/punctuation separate words)
words = re.findall(r'\b\S+\b', content)

# Check spelling and collect misspelled words
misspelled_words = [word for word in words if word not in dzongkha_words]

if misspelled_words:
    print("Misspelled words found:", misspelled_words)
else:
    print("No misspelled words found.")
