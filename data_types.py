
text = input("Введите текст:")

unique = list(set(text))

print("Количество уникальных символов: ", len(unique))

L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))

a = 5
b = 3+2
print(id(a))
print(id(b))


list_1 = ['a', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)
print(list_1)
print(list_2)
print(list_3)

print(list_1 == list_2)
print(list_1 == list_3)

print(list_1 is list_2)
print(list_1 is list_3)

L = ['Hello', 'world']
M = L

print(M is L)
# True
M.append('!')

print(L)
# ['Hello', 'world', '!']
M = L.copy()

print(M is L)
# False


shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])
print(shopping_center[-1])
shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print(list_id_before == list_id_after)


# можно проверить, находится ли число 1 в промежутке (0,4)
cond1 = 0 < 1
cond2 = 1 < 4

print(cond1 and cond2)
# True

# или, например, содержат ли две строки один и тот же символ
cond3 = 't' in "python"
cond4 = 't' in "django"

print(cond3 and cond4)
# False


print(not True)
# False

print(not False)
# True


# к слову, логические выражения можно сразу объединять в одно целое
print(('t' in "python") or ('t' in "django"))
# True

print("1. Дано целое число 123456789. Определите, входит ли в него цифра 5.")
print('5' in str(123456789)) # True

print("2. Дано n-значное целое число N. Определите, входят ли в него цифры 3 и 7.")
N = 1234567898
print('3' in str(N) and '7' in str(N)) # True

print("3. Эквивалентные объекты всегда равны. Но равные объекты не всегда эквивалентны:")
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

a is None # Хорошо

a == None # Плохо


