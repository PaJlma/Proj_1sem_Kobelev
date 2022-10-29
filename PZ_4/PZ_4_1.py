def program():
    try:
        N = int(input("Введите число: "))
        answer = 0
        i = 0

        while i != N:
            i += 1
            answer += 1 / i

        for i in range(1, N+1):
            answer += 1/i

        print(answer)

    except ValueError:
        print("Ошибка ввода")
        program()

program()