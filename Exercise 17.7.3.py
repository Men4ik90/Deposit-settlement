money = float(input('Введите сумму:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = {'ТКБ': (5.6 * (money)/100)+(money),
           'СКБ': (5.9* (money)/100)+(money),
           'ВТБ': (4.28* (money)/100+(money)),
           'СБЕР': (4.0* (money)/100+(money))} # Расчет накопленных средства за год вклада в каждом из банков (депозит + процент за год)

print(deposit)# Вывод информации о накопленных средствах за год вклада в каждом из банков (депозит + процент за год)
print("-" * 40)
r =0
for k in deposit:
    if deposit[k]> r:
        deposit_i =deposit[k]
        # deposit_i= k
print("Максмальная сумма, которую Вы можете зарабоать-",deposit_i)
