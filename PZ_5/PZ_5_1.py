'''
Составить программу, в которой функция генерирует четырехзначное число и
определяет, есть ли в числе одинаковые цифры.
'''

import random

def foo():
    num = str(random.randint(1000, 9999))
    nCount = 0

    numbers = list(num) #Строка разбивается в массив, для дальнейшего поиска совпадений с помощью count()
    repeat = [] #Массив в который будут записываться повторяющиеся цифры

    '''
    Ниже цикл проходится по записанным в массив numbers цифрам
    и ищет совпадения с помощью count().
    Если совпадений больше чем кол-во цифр в числе, то это значит,
    что в числе есть повторяющиеся цифры
    '''

    for number in numbers:
        nCount += num.count(number)
        if num.count(number) > 1:
            repeat.append(number)

    if nCount > len(numbers):
        return f'Число: {num} | Есть повторения | Число повторений: {int((nCount - len(numbers))/2)} | Повторяются цифры: {set(repeat)}'
    else:
        return f'Число: {num} | Нет повторений'

print(foo())