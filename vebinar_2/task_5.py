# Среди трёх числел (принимаются на ввод) найти среднее.

print("Введите три целых числа: ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if b < a < c or c < a < b:
    print("Среднее:", a)
elif a < b < c or c < b < a:
    print("Среднее:", b)
else:
    print("Среднее:", c)
