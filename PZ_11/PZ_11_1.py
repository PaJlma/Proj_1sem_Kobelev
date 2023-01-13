file1 = open('file1.txt', 'w')
file1.write('-9 -8 -7 -6 -5 -4 -3 -2 -1 1 2 3 4 5 6 7 8 9')
file1.close()

with open('file1.txt', 'r') as file1:
    source = file1.readline()

sourceList = source.split()

for sourceOne in sourceList:
    int(sourceOne)

sourceMax = max(sourceList)
indexOfMax = sourceList.index(sourceMax)

lenghtOfList = len(sourceList)
thirdList = lenghtOfList / 3


print(f'Исходные данные: {source}\n'
      f'Кол-во элементов: {len(sourceList)}\n'
      f'Индекс последнего максимального элемента: {indexOfMax}\n'
      f'{int(thirdList)}')
