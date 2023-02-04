'''
В матрице элементы второго столбца заменить элементами из одномерного
динамического массива соответствующей размерности.
'''

import random

matrix = [[], []] #Объявление матрицы, т.е двух списков в одном списке
list = []

for i in range(0, random.randint(5, 15)):
    matrix[0].append(random.randint(0, 25))
    matrix[1].append(random.randint(0,25)) #Заполнение матрицы и одномерного массива
    list.append(random.randint(0, 15))

print(f'Матрица до изменения:\n'
      f'{matrix[0]}\n'
      f'{matrix[1]}\n'
      f'Одномерный массив: {list}\n')

matrix[1] = [i for i in list]

'''
Выше
Списковым включением заменяем элементы второго списка матрицы
элементами одномерного массива
'''

print(f'Матрица после изменения:\n'
      f'{matrix[0]}\n'
      f'{matrix[1]}\n'
      f'Одномерный массив: {list}\n')