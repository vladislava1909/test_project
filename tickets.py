t_count = int(input("Введите количество билетов: "))
if t_count == 0:
    print("Сумма к оплате: 0 руб.")
else:
    total_sum = 0
    for i in range(1, t_count + 1):
        age = int(input("Введите возраст посетителя {}: ".format(i)))
        if age < 18:
            sum_t = 0
        elif 18 <= age < 25:
            sum_t = 990
        else:
            sum_t = 1390
        total_sum += sum_t
    if t_count > 3:
        total_sum = total_sum - total_sum * 0.1
print("Сумма к оплате: {} руб.".format(total_sum))
