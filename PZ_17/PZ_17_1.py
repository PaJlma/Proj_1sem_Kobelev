'''
Создайте класс "Калькулятор" с методами "сложение", "вычитание", "умножение" и
"деление". Каждый метод должен принимать два аргумента и возвращать результат
операции.
'''

class Calculator:
    @staticmethod
    def sum(first, second):
        return first + second

    @staticmethod
    def substract(first, second):
        return first - second

    @staticmethod
    def multiply(first, second):
        return first * second

    @staticmethod
    def division(first, second):
        if second != 0:
            return first / second
        else:
            return ValueError('Нельзя делить на ноль!')

print(Calculator.sum(2, 2))
print(Calculator.substract(2, 2))
print(Calculator.multiply(2, 2))
print(Calculator.division(2, 2))
print(Calculator.division(2, 0))