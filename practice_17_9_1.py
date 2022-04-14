def qsort(array, left, right):  # функция быстрой сортировки
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


def valid_array_txt(array_txt):  # функция проверки соответствия условиям ввода данных
    array_str = array_txt.strip().split(' ')
    for item in array_str:
        try:
            int(item)
        except Exception as ex:
            return False
    return True

array_txt = ''
is_valid_input = False
while is_valid_input is not True:
    array_txt = input("Введите последовательность целых чисел через пробел: ")
    is_valid_input = valid_array_txt(array_txt)
    if is_valid_input is not True:
        print("Введены некорректные данные! Попробуйте снова.")


idx_input_digit = int(input("Введите любое целое число: "))
array = array_txt.strip().split(' ')

for i in range(len(array)):
    array[i] = int(array[i])

qsort(array, 0, len(array) - 1)
print("Последовательность после сортировки:", array)

if idx_input_digit < array[0] or idx_input_digit > array[-1]:
    print("Введенное число выходит за границы последовательности!")
    exit()

if idx_input_digit == array[0]:
    print("Введенное число является минимальным в последовательности!")
    exit()

if idx_input_digit == array[-1]:
    print("Введенное число является максимальным в последовательности!")
    exit()

for i in range(len(array) - 1):
    value_1 = array[i]
    value_2 = array[i + 1]
    if value_1 < idx_input_digit <= value_2:
        print("Индекс числа, который меньше введенного пользователем числа, \nа следующий за ним больше или равен этому числу:", i)
        break












