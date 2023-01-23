'''
Средствами языка Puthon сформировать текстовый файл (txt, содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (txt следующего вида, предварительно выполнив требуемую
обработку элементов:

Исходные данные:
Количество элементов:
Индекс последнего максимального элемента:
Меняем местами первую и последнюю трети:
'''

import random

file1 = open('file1.txt', 'w')
nums = []

for i in range(0, random.randint(10, 30)):
    nums.append(str(random.randint(1, 15))) #Заполнение массива

numsStr = ' '.join(nums) #Преобразование массива в строку для заполнения файла

file1.writelines(numsStr) #Запись в файл
file1.close()

with open('file1.txt', 'r') as file1:
    source = file1.readline() #Чтение всего файла (все записи в строке)

sourceList = source.split() #Разбивка строки на список

maxNum = 0
indexOfMaxNum = 0
sourceListInt = list(map(int, sourceList))

'''
Цикл ниже проходится по всему списку и если элемент равен или больше предыдущему максимальному значению,
то он становится новым максимальным значением,
при этом поиск происходит с индекса предыдущего максимального числа
'''

for i in sourceListInt:
    if i >= maxNum:
        maxNum = i
        try:
            indexOfMaxNum = sourceListInt.index(maxNum, indexOfMaxNum+1)
        except:
            pass
    else:
        pass

lenghtOfList = len(sourceList)
thirdList = int(lenghtOfList / 3)

'''
Здесь длина массива делится на три и в цикле ниже
цикл меняет значения массива с индексами от нуля до трети списка с двух сторон
'''

for i in range(0, thirdList+1):
    sourceListInt[i], sourceListInt[-i-1] = sourceListInt[-i-1], sourceListInt[i]


print(f'Исходные данные: {source}\n'
      f'Кол-во элементов: {len(sourceList)}\n'
      f'Индекс последнего максимального элемента: {indexOfMaxNum} {maxNum}\n'
      f'Поменяные первая и последняя треть: {sourceListInt}')
