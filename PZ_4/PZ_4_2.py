'''
Дано число А (> 1). Вывести наименьшее из целых чисел К, для которых сумма 1 +
1/2 +... + 1/K будет больше А, и саму эту сумму.
'''

def program():
    try:
        A = int(input("Введите число A: "))
        answer = 0
        i = 0

        while A > answer:
            i += 1
            answer += 1/i
            print(f"Iteration: {i}")


        print(f"Ответ был числом {i}, сумма деления на единицу этого числа - {answer}")

    except ValueError:
        print("Ошибка ввода")
        program()

program()