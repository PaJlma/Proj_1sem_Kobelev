def program(): #Функция для возврата
    try:
        first = float(input("Введите первое число: ")) #Ввод данных
        second = float(input("Введите второе число: "))

        choice = int(input("Введите число, обозначающее действие, которое вы хотите выполнить\n1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление (второе число не должно равняться нулю)\n"))

        '''
        Сверху выбор действия
        '''
        if choice == 1 :
            print(first + second)

        elif choice == 2:
            print(first - second)

        elif choice == 3:
            print(first * second)

        elif choice == 4 and second != 0:
            print(first / second)

        else:
            print("Неизвестное значение")
            program() #возврат

    except ValueError: #при ошибке
        print("Ошибка ввода данных")
        program()

program() #запуск программы с помощбю функции