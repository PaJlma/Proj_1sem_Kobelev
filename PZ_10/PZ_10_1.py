'''
В магазинах имеются следующие товары. Магнит — молоко, соль, сахар. Пятерочка —
мясо, молоко, сыр. Перекресток — молоко, творог, сыр, сахар. Определить:

1. полный список всех товаров.
2. в каких магазинах можно приобрести одновременно молоко и сыр.
3. в каких магазинах можно приобрести сахар.
'''

magnit = {'молоко', 'соль', 'сахар'}
pyaterochka = {'мясо', 'молоко', 'сыр'}
perekrestok = {'молоко', 'творог', 'сыр', 'сахар'}
allShops = [magnit, pyaterochka, perekrestok]
findMilkAndCheese = []
findSugar = []

fullList = magnit | pyaterochka | perekrestok

for shop in allShops:
    if 'сыр' and 'молоко' in shop:
        findMilkAndCheese.append(shop)

for shop in allShops:
    if 'сахар' in shop:
        findSugar.append(shop)

print(fullList)
print(findMilkAndCheese)
print(findSugar)