# Факториал 1.
n = int(input("Введите целое число:"))
factorial = 1

while n > 1:
    factorial *= n
    n -= 1
print(factorial)

# Факториал 2.

n = int(input("Введите целое число:"))
factorial = 1

for i in range(2,n + 1):
    factorial *= i
print(factorial)



