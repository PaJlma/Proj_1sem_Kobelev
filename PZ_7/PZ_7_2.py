'''
Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов
(путь), собственно имя и расширение. Выделить из этой строки имя файла (без
расширения).
'''

def program():
  try:
    path = input('Введите имя файла: ').replace('/', '\\')
    lastSlesh = path.rfind('\\') #находится последний слэш и строка обрезается до него
    noSlesh = path[lastSlesh+1:]
    findDot = noSlesh.find('.') #находится точка и строка обрезает справа до нее
    fileName = noSlesh[:findDot]

    print(f'File name is: {fileName}')

  except ValueError:
    program()
    print('Ошибка ввода')

program()