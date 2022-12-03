'''
Вариант 9. Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая
средние температуры по месяцам в году. Преобразовать информацию из строки в
словарь, с использованием функции найти среднюю и минимальные температуры,
результаты вывести на экран.
'''

string = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'
splited = string.split()

temperatures = []

for i in range(1, len(splited)): # В массив записываются все значения кроме года
  temperatures.append(int(splited[i]))

lst = {
    'year': splited[0].replace('год', ''),
    'temp': temperatures,
}

def middleNumbers(lst):
  coof = len(lst)
  for i in lst:
    i += i

  middle = round(i/coof)
  return middle

print(f'Год: {lst["year"]}')
print(f'Среднее значение температур за год: {middleNumbers(lst["temp"])}')
print(f'Минимальное значение за год: {min(lst["temp"])}')