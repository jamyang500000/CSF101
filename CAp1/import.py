import re

link = "https://csf101-server-cap1.onrender.com/get/input/341"
file = re.get(link)
with open('341.txt', 'wb') as file:
    data = file.write(file.content)
print('Downloaded:341.txt')