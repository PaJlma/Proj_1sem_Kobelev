'''
В магазинах имеются следующие товары. Магнит — молоко, соль, сахар. Пятерочка —
мясо, молоко, сыр. Перекресток — молоко, творог, сыр, сахар. Определить:

1. полный список всех товаров.
2. в каких магазинах можно приобрести одновременно молоко и сыр.
3. в каких магазинах можно приобрести сахар.
'''

magnit = {
    'name': 'magnit',
    'asort': {'молоко', 'соль', 'сахар'},
}
pyaterochka = {
    'name': 'pyaterochka',
    'asort': {'мясо', 'молоко', 'сыр'},
}
perekrestok = {
    'name': 'perekrestok',
    'asort': {'молоко', 'творог', 'сыр', 'сахар'},
}
allShops = [magnit, pyaterochka, perekrestok]
findMilkAndCheese = []
findSugar = []

fullList = magnit['asort'] | pyaterochka['asort'] | perekrestok['asort']

for shop in allShops:
    if 'молоко' in shop['asort'] and 'сыр' in shop['asort']:
        findMilkAndCheese.append(shop['name'])

for shop in allShops:
    if 'сахар' in shop['asort']:
        findSugar.append(shop['name'])


print(f'Полный список товаров: {fullList}\nВ этих магазинах можно одновременно купить сыр и молоко: {findMilkAndCheese}\n'
      f'В этих магазинах можно купить сахар: {findSugar}')