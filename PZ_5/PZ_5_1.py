'''
Составить программу, в которой функция генерирует четырехзначное число и
определяет, есть ли в числе одинаковые цифры.
'''

import random

def foo():
    num = str(random.randint(1000, 10000))

    numbers = list(num)

    for number in numbers:
        if num.count(number) > 1:
            return num, 'Да - Пизда'
        else:
            return num, 'Нет - Пидора ответ'

print(foo())