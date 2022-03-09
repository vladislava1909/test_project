per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input('Enter deposit amount: ')
deposit = []

for i in per_cent.values():
    deposit_money = float(i) * int(money) / int(100)
    deposit.append(int(deposit_money))

print("deposit =", deposit)
print("Максимальная сумма, которую вы можете заработать =", max(deposit))





