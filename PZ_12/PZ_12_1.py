'''
Даны две последовательности. Найти элементы, общие для двух
последовательностей и их количество.
'''

import random

lst1 = []
lst2 = []

for i in range(0, random.randint(5, 25)):
    lst1.append(random.randint(0, 25))

for i in range(0, random.randint(5, 25)):
    lst2.append(random.randint(0, 25))

print(f'Исходные последовательности:\n'
      f'{lst1}\n'
      f'{lst2}')

repeat = [i for i in lst1 if i in lst2]
repeatLen = len(repeat)

print(f'Повторяющиеся значения: {repeat}\n'
      f'Их кол-во: {repeatLen}')