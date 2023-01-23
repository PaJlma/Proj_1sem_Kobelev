'''
Из предложенного текстового файла (text18-9.txt вывести на экран его содержимое,
количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
в стихотворной форме предварительно поставив последнюю строку фразой введенной
пользователем.
'''

with open('text18-9.txt') as file:
    source = file.readline()

print(f'Исходник: {source}\n'
      f'Кол-во строчный символов: {sum(map(str.islower, source))}') #Считывается количество строчных символов

sourceStih = ['Sun of the sleepless! Melancholy star!', 'Whose tearful beam glows tremulously far,',
             'That showst the darkness thou canst not dispel,', 'How like art thou to joy rememberd well!']

stihExpended = sourceStih
text = input('Введите последнюю строчку стиха: ')
stihExpended.append(text)

stihFile = open('stih.txt', 'w')
for line in stihExpended:
    stihFile.write(line + '\n') #Построчный ввод
stihFile.close()

with open('stih.txt', 'r') as file: #Построчные чтение
    for line in file:
        print(line)