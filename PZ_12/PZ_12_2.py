'''
Из заданной строки отобразить только символы нижнего регистра. Использовать
библиотеку string. Строка: In Pycharm, you can specify third-party standalone applications and run them as External Tools
'''

from string import ascii_lowercase

str = 'In Pycharm, you can specify third-party standalone applications and run them as External Tools'

strLower = [i for i in str if i in ascii_lowercase]

print(strLower)