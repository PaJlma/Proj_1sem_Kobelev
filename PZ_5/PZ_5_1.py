'''
Составить программу, в которой функция генерирует четырехзначное число и
определяет, есть ли в числе одинаковые цифры.
'''

import random

def foo():
    num = random.randint(1000, 9999)
    numStr = str(num)
    nCount = 0

    '''
    Ниже цикл на каждой итерации как бы "отрезает" правую цифру числа
    и сравнивает её с исходным числом, ища повторения с помощью count()
    '''

    iter = 0
    numRaw = num

    while iter < 4:
        num = numRaw % 10
        numRaw = numRaw // 10
        nCount += numStr.count(str(num))
        iter += 1

    if nCount > 4:
        return f'Число: {numStr} | Есть повторения'
    else:
        return f'Число: {numStr} | Нет повторений'

print(foo())