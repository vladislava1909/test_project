print("1. Генератор списков, "
      "в котором будут храниться квадраты первых десяти натуральных чисел.")
squares = [i**2 for i in range(1,11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("2. список будут включаться квадраты только от нечетных чисел.")
squares = [i**2 for i in range(1,11) if i % 2 == 1]
# [1, 9, 25, 49, 81]

print("3. составить список из кортежей:")
list_tuples = [(i, i**2) for i in range(1,11)]
#[(1, 1),
# (2, 4),
# (3, 9),
# (4, 16),
# (5, 25),
# (6, 36),
# (7, 49),
# (8, 64),
# (9, 81),
# (10, 100)]

print("4. используя вложенные генераторы списков можно создать матрицу ")
M = [[i+j for j in range(5)] for i in range(5)]
#[[0, 1, 2, 3, 4],
# [1, 2, 3, 4, 5],
# [2, 3, 4, 5, 6],
# [3, 4, 5, 6, 7],
# [4, 5, 6, 7, 8]]

print("5. При помощи генератора списков создайте таблицу умножения чисел от 1 до 10. ")
T = [[i*j for j in range(1,11)] for i in range(1,11)]

print("6. в сочетании использования генераторов списков и функции input()."
      " На каждой итерации цикла консоль будет запрашивать данные для ввода и сохранять их в качестве элемента списка.")
L = [input("Ведите данные: ") for i in range(5)]
print(L)

print("7. преобразование в необходимый тип")
L = [int(input("Введите число: ")) for i in range(5)]
print(L)

print("8. Модифицируйте последний пример таким образом, "
      "чтобы в список сохранялось True, если элемент четный,"
      " и False, если элемент нечетный.")
L = [int(input("Введите число: ")) % 2 == 0 for i in range(5)]
print(L)

print("9.записать логическое выражение, используя all([ ]) и any([ ]) над списком четности, "
      "если его результат будет истинным тогда и только тогда, "
      "когда в списке есть хотя бы один четный и хотя бы один нечетный элемент.")
L = [int(input("Введите число: ")) % 2 == 0 for i in range(5)]
any(L) and not all(L)
print(L)

print("10. В Python существует функция zip()")
L = [i for i in range(10)]
# 0 1 2 3 4 5 6 7 8 9
M = [i for i in range(10,0,-1)]
# 10 9 8 7 6 5 4 3 2 1

for a, b in zip(L,M):
    print('a =', a, 'b =', b, 'c =', a*b)

print("11. Используя функцию zip() внутри генераторов списков, "
      "вычислите поэлементные произведения списков L и M.")
L = [i for i in range(10)]
# 0 1 2 3 4 5 6 7 8 9
M = [i for i in range(10,0,-1)]
# 10 9 8 7 6 5 4 3 2 1

N = [a*b for a,b in zip(L,M)]
print(N)

print("12.Реализуйте программу, которая сжимает последовательность символов. "
      "На вход подается последовательность вида: aaabbccccdaa"
      "Необходимо вывести строку, состоящую из символов и количества повторений этого символа. "
      "Вывод должен выглядеть как: a3b2c4d1a2")
text = input("Введите строку: ")  # получаем строку

first = text[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку

for c in text:
      if c == first:  # если символ совпадает с сохраненным,
            count += 1  # то увеличиваем счетчик
      else:
            result += first + str(count)  # иначе - записываем в результат
            first = c  # и обновляем сохраненный символ с его счетчиком
            count = 1

result += first + str(count)  # и добавляем в результат последний символ
print(result)