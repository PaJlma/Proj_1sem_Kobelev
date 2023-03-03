import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    data = file.read()

    lastNamesPattern = re.compile(r'(?i)\bДостоевс\w*')
    lastNames = re.findall(lastNamesPattern, data)
    print(lastNames)