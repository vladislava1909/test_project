per_cent = {
    'ТКБ': 5.6,
    'СКБ': 5.9,
    'ВТБ': 4.28,
    'СБЕР': 4.0
}
print("Процентные ставки банков:")
for k, v in per_cent.items():
    print(f"{k}: {v}")
money = float(input('Введите сумму депозита: '))
print('Сумма, которую вы заработаете в каждом банке:')
for k, v in per_cent.items():
    print(f"{k}: {round(v*money/100, 2)}")
r = 0
for k in per_cent:
    if per_cent[k] > r:
        r = per_cent[k]
        m = k
print('Максимальная сумма, которую вы можете заработать:', m, round(r * money / 100, 2))