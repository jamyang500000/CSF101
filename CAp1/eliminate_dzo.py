import re

file_path = "dzongkha.txt"

with open(file_path, "r",encoding="utf-8") as file:
    Dict = file.read()

cleaned_Dict = re.sub(r'[a-zA-Z-0-9]+|[^\w\s]', '', Dict)

with open(file_path, "w",encoding="utf-8") as file:
    file.write(cleaned_Dict)

print("English word, puntuations and numbers removed")

