print("20. Модифицируйте алгоритм быстрой сортировки таким образом, "
      "чтобы ведущий элемент выбирался как случайный среди подмассива, "
      "который сортируется на данном этапе. Воспользуйтесь функцией из пакета random.")
import random


def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    count = 0
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

qsort_random(array, 0, len(array) - 1)
print(array)






