'''
Дано целое число М (>0). Найти сумму [ 1 + 1/2 + 1/3 +...+ 1/N ]
'''

def program():
    try:
        N = int(input("Введите число: "))
        answer = 0
        i = 0

        while i != N:
            i += 1
            answer += 1 / i

        print(answer)

    except ValueError:
        print("Ошибка ввода")
        program()

program()