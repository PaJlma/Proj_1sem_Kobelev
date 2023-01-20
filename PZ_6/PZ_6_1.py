'''
Дан целочисленный список размера 10. Вывести вначале все содержащиеся в данном
списке четные числа в порядке возрастания их индексов, а затем — все нечетные
числа в порядке убывания их индексов.
'''

import random

iter = 0
list = []

while iter < 10: #Заполнение массива
    list.append(random.randint(0, 100))
    iter += 1

print(f'Массив: {list}')

iter = 0

print('Чётные числа в порядке возрастания:')

while iter < len(list):
    if list[iter] % 2 == 0:
        print(list[iter])
    iter += 1

iter = len(list) - 1

print('Нечётные числа в порядке убывания:')

while iter >= 0:
    if list[iter] % 2 != 0:
        print(list[iter])
    iter -= 1