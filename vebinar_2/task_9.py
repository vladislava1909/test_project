# Посчитать четные и нечетные цифры числа.
# Определить сколько в числе четных цифр, а сколько нечетных.
# Число вводится с клавиатуры.
a = int(input("Введите целое число:"))
even = 0
odd = 0

while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10
print("Even: %d, Odd: %d" % (even, odd))
