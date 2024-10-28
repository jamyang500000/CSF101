import string

# Define invalid characters (English alphabets, numbers, and punctuation)
invalid_chars = string.ascii_letters + string.digits + string.punctuation

# Read the content of the file
with open('dzongkha.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Filter out the invalid content
filtered_content = ''.join(char for char in content if char not in invalid_chars)

# Write the filtered content to a new file
with open('dzongkha_only.txt', 'w', encoding='utf-8') as file:
    file.write(filtered_content)

print("Filtered content has been written to 'dzongkha_only.txt'")
