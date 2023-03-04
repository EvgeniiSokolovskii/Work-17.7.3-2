per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму: '))
dep=[]
for value in per_cent: dep.append(int(per_cent[value]*money/100))
deposit = max(dep)
print('Максимальная сумма, которую вы можете заработать -',deposit)
