'''
Дано множество А из N точек на плоскости и точка В (точки заданы своими
координатами х, у). Найти точку из множества А, наиболее близкую к точке В.
Расстояние R между точками с координатами (х1, у1) и (х2, у2) вычисляется по
формуле:

R = sqrt((x2 —х1)^2 + (y2 — у1)^2).

Для хранения данных о каждом наборе точек следует использовать по два списка: первый
список для хранения абсцисс, второй — для хранения ординат.

Пятница - dead line
'''

from math import sqrt
from random import randint

def program():
    try:
        RANGE = int(input('Введите число точек: '))

        x = []
        y = []

        answers = []

        for i in range(1, RANGE + 1): #Рандомно генерируются координаты точек
            x.append(randint(1, 10))
            y.append(randint(1, 10))

        print(f'x:{x}\ny:{y}')

        b = [randint(1, 10), randint(1, 10)] #Рандомно генерируется точка B

        i = 0
        j = 0

        while i <= len(x)-1 and j <= len(y)-1:
            r = sqrt(((b[0] - x[i]) ** 2) + ((b[1] - y[i]) ** 2)) #формула по которой вычисляется расстояние
            answers.append(r) #Все расстояние загружются в массив
            i += 1
            j += 1


        '''
        Ниже из всех расстояний выбирается наименьшее и находится индекс этого значения в массиве answers
        с помощью которого вычисляются координаты точек из которых было вычисленно это расстояние
        '''

        # r = sqrt(((b[0] - x[0])**2) + ((b[1] - y[0])**2))
        print(f'Все расстояния: {answers}')
        indexOfAnswers = answers.index(min(answers))

        print('\n\n')

        print(f'Точка с координатами ({x[indexOfAnswers]}; {y[indexOfAnswers]}) является ближайшей к точке B с координатами ({b[0]}; {b[1]})\n'
              f'Расстояние до точки: {min(answers)}')

    except ValueError:
        print('Ошибка ввода')
        program()

program()