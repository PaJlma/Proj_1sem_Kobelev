'''
В матрице найти среднее арифметическое положительных элементов, кратных 3.
'''

import random
from functools import reduce

matrix = [[], [], []]
list = []

for i in range(0, random.randint(5, 25)):
    matrix[0].append(random.randint(-25, 25))
    matrix[1].append(random.randint(-25, 25))
    matrix[2].append(random.randint(-25, 25))

for str in matrix:
    list = list + [i for i in str] #Представление матрицы в одномерном массиве

filtered = [i for i in list if i % 3 == 0 and i > 0] #Отфильтровывание через списковое включение

if len(filtered) != 0:
    sum = reduce(lambda x, y: x + y, filtered) #Сумма всех элементов отфильтрованного массива
    average = sum/len(filtered) #Вычисление среднего арифметического

    print(f'Исходная матрица:\n'
          f'{matrix[0]}\n'
          f'{matrix[1]}\n'
          f'{matrix[2]}\n'
          f'Отфильтрованная матрица со значениями, кратными 3: {filtered}\n'
          f'Среднее арифмметическое: {average}')

else:
    print('Фильтр не нашёл элементов, кратных 3')