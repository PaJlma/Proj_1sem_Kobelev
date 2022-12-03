'''
Дан список размера N. Найти количество участков, на которых его элементы
монотонно убывают.
'''

import random  # Импортируем библиотеку random
def program():
    try:
        lst = [random.randint(1, 100) for el in range(int(input('Введите размер списка: ')))]
        # Заполняем список размера N, рандомными значениями
        print(lst)  # Выводим созданный список на экран
        result = 0
        count = 0
        for j in range(len(lst) - 2):
            if lst[j + 2] < lst[j + 1] < lst[j]:
                count += 1
            elif count >= 1 and lst[j + 1] < lst[j + 2]: # Поиск монотонных возрастаний
                result += 1
                count = 0
        if lst[-1] < lst[-2] < lst[-3]:
            result += 1     # Запись кол-ва элементов возрастания
        print(f'Ответ: {result}')  # Вывод результата

    except ValueError:
        print("Ошибка ввода")  # Оповещание об ошибке
        program()  # Повторный вызов функции из-за ошибки


program()