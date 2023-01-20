import random

file1 = open('file1.txt', 'w')
nums = []

for i in range(0, random.randint(10, 20)):
    nums.append(str(random.randint(1, 5)))

numsStr = ' '.join(nums)

file1.writelines(numsStr)
file1.close()

with open('file1.txt', 'r') as file1:
    source = file1.readline()

sourceList = source.split()

sourceMax = max(sourceList[::-1], key=lambda i: int(i))
indexOfMax = sourceList.index(sourceMax)

lenghtOfList = len(sourceList)
thirdList = lenghtOfList / 3


print(f'Исходные данные: {source}\n'
      f'Кол-во элементов: {len(sourceList)}\n'
      f'Индекс последнего максимального элемента: {indexOfMax} {sourceMax}\n'
      f'{int(thirdList)}')
