'''
В исходном текстовом файле(Dostoevsky.txt найти все варианты фамилии
Достоевского (т.е. с различными окончаниями, например, Достоевский,
Достоевского) в единственном экземпляре.
'''

import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    data = file.read()

    lastNamesPattern = re.compile(r'(?i)\bДостоевс\w*') #Создание паттерна поиска
    lastNames = re.findall(lastNamesPattern, data) #Поиск фамилий
    lastNames = set(lastNames) #Удаление фамилий с однинаковыми склонениями
    print(lastNames)