print("1. Напишем функцию par_checker(string), "
      "которая проверяет строку string на корректность расстановки скобок.")


def par_checker(string):
    stack = []  # Инициализируем стек

    for s in string:  # Читаем строку посимвольно
        if s == "(":  # Если открывающая скобка,
            stack.append(s)  # Добавляем её в стек
        elif s == ")":  # если встретилась закрывающая скобка, то проверяем
            if len(stack) > 0 and stack[-1] == "(":  # пуст ли стек и является ли верхний элемент - открывающей скобкой
                stack.pop()  # удаляем из стека
            else:  # иначе
                return False  # завершаем функцию False
    return len(stack) == 0


# Если стек пустой, то незакрытых скобок не осталось. Значит возвращаем True, иначе - False.


print(par_checker("(5+6)*(7+8)/(4+3)"))

print("2. Модифицируйте функцию проверки баланса скобок для двух видов скобок: круглых и квадратных.")

pars = {")": "(", "]": "["}


def par_checker_mod(string):
    stack = []

    for s in string:
        if s in "([":
            stack.append(s)
        elif s in ")]":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(par_checker_mod("(5+6)*(7+8)/[4+3]"))

print("3. Попробуем создать обработчик задач на бесконечном цикле с использованием очереди:")

N_max = int(input("Определите размер очереди: "))

queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
order = 0  # будем хранить сквозной номер задачи
head = 0  # указатель на начало очереди
tail = 0  # указатель на элемент следующий за концом очереди


def is_empty():  # очередь пуста?
    # да, если указатели совпадают и в них содержится ноль
    return head == tail and queue[head] == 0


def size():  # получаем размер очереди
    if is_empty():  # если она пуста
        return 0  # возвращаем ноль
    elif head == tail:  # иначе, если очередь не пуста, но указатели совпадают
        return N_max  # значит очередь заполнена
    elif head > tail:  # если хвост очереди сместился в начало списка
        return N_max - head + tail
    else:  # или если хвост стоит правее начала
        return tail - head


def add():  # добавляем задачу в очередь
    global tail, order
    order += 1  # увеличиваем порядковый номер задачи
    queue[tail] = order  # добавляем его в очередь
    print("Задача № %d добавлена" % (queue[tail]))
    # увеличиваем указатель на 1 по модулю максимального числа элементов
    # для зацикливания очереди в списке
    tail = (tail + 1) % N_max
    print(tail)


def show():  # выводим приоритетную задачу
    print("Задача № %d в приоритете" % (queue[head]))


def do():  # выполняем приоритетную задачу
    global head
    print("Задача № %d выполнена" % (queue[head]))
    queue[head] = 0  # после выполнения приравниваем к 0 элемент по указателю
    head = (head + 1) % N_max  # и циклично перемещаем указатель


while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", size())
    elif cmd == "add":
        if size() != N_max:
            add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if is_empty():
            print("Очередь пустая")
        else:
            show()
    elif cmd == "do":
        if is_empty():
            print("Очередь пустая")
        else:
            do()
    elif cmd == "exit":
        for _ in range(size()):
            do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")

print("4.  Давайте попробуем представить часть схемы метрополитена г. Санкт-Петербурга в виде списка смежности.")

K = {"Лиговский проспект":
         ["Площадь Александра Невского 2"],
     "Площадь Александра Невского 2":
         ["Площадь Александра Невского 1",
          "Лиговский проспект",
          "Новочеркасская"],
     "Площадь Александра Невского 1":
         ["Площадь Александра Невского 2",
          "Елизаровская"],
     "Новочеркасская":
         ["Площадь Александра Невского 2",
          "Ладожская"],
     "Ладожская":
         ["Новочеркасская",
          "Проспект Большевиков"],
     "Проспект Большевиков":
         ["Ладожская",
          "Дыбенко"],
     "Дыбенко":
         ["Проспект Большевиков"]}

print("5.  Представьте эту часть схемы в виде графа и создайте список смежности, используя словарь.")

N = {"Адмиралтейская":
         ["Садовая"],
     "Садовая":
         ["Сенная площадь",
          "Спасская",
          "Адмиралтейская",
          "Звенигородская"],
     "Сенная площадь":
         ["Садовая",
          "Спасская"],
     "Спасская":
         ["Садовая",
          "Сенная площадь",
          "Достоевская"],
     "Звенигородская":
         ["Пушкинская",
          "Садовая"],
     "Пушкинская":
         ["Звенигородская",
          "Владимирская"],
     "Владимирская":
         ["Достоевская",
          "Пушкинская"],
     "Достоевская":
         ["Владимирская",
          "Спасская"]}

print("6.  Возьмите граф из предыдущего задания (с картой метро) "
      "и постройте из него взвешенный граф. "
      "В качестве весов используйте время, необходимое для того, "
      "чтобы доехать (или перейти) с одной станции на другую.")
print("7. поиск кратчайшего пути от одной вершины к другой. ")
print("8. Модифицируйте алгоритм Дейкстры таким образом, "
      "что в массив P по соответствующему ключу будет записываться предок"
      " с минимальным расстоянием, если это необходимо. ")

G = {"Адмиралтейская":
         {"Садовая": 4},
     "Садовая":
         {"Сенная площадь": 3,
          "Спасская": 3,
          "Адмиралтейская": 4,
          "Звенигородская": 5},
     "Сенная площадь":
         {"Садовая": 3,
          "Спасская": 3},
     "Спасская":
         {"Садовая": 3,
          "Сенная площадь": 3,
          "Достоевская": 4},
     "Звенигородская":
         {"Пушкинская": 3,
          "Садовая": 5},
     "Пушкинская":
         {"Звенигородская": 3,
          "Владимирская": 4},
     "Владимирская":
         {"Достоевская": 3,
          "Пушкинская": 4},
     "Достоевская":
         {"Владимирская": 3,
          "Спасская": 4}}


D = {k: 100 for k in G.keys()}  # расстояния
start_k = 'Адмиралтейская'  # стартовая вершина
D[start_k] = 0  # расстояние от неё до самой себя равно нулю
U = {k: False for k in G.keys()}  # флаги просмотра вершин
P = {k: None for k in G.keys()}  # предки

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key=lambda x: D[x])

    for v in G[min_k].keys():  # проходимся по всем смежным вершинам
        if D[v] > D[min_k] + G[min_k][v]:  # если расстояние от текущей вершины меньше
            D[v] = D[min_k] + G[min_k][v]  # то фиксируем его
            P[v] = min_k  # и записываем как предок
    U[min_k] = True  # просмотренную вершину помечаем

print(D)

pointer = "Владимирская"  # куда должны прийти
while pointer is not None:  # перемещаемся, пока не придём в стартовую точку
    print(pointer)
    pointer = P[pointer]


print("9. Мы создали класс узла, а в конструкторе записали значение, "
      "которое должно храниться в нём. Также инициализировали левого и правого потомка. "
      "Пока что в них ничего не хранится — нужно иметь процедуру вставки новых элементов."
      " Напишем разные методы для вставки на место левого потомка и на место правого потомка.")


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self
# Поясним, что здесь произошло. Если в текущем узле нет левого потомка,
# то новый узел вставляем на его место. Если левый потомок уже существует
# — он становится таким же левым потомком, но уже нового узла. Иными словами,
# он остается левым, но его глубина увеличивается. Аналогично поступим с правым.

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    def pre_order(self):  # префиксный обход
        print(self.value)  # процедура обработки

        if self.left_child is not None:  # если левый потомок существует
            self.left_child.pre_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.pre_order()  # рекурсивно вызываем функцию

    def post_order(self):  # метод постфиксного обхода в глубину.
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.post_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.post_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

    def in_order(self):  # Метод инфиксного обхода в глубину
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.in_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.in_order()  # рекурсивно вызываем функцию


# создаём корень и его потомков /7|2|5\
node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)

print("Префиксный обход: ")
node_root.pre_order()
print("Постфиксный обход: ")
node_root.post_order()
print("Инфиксный обход: ")
node_root.in_order()


print("10. Сейчас мы попробуем создать класс LinkedList, реализующий список."
      " Элементы списка будут представлять собой экземпляры класса Node.")


class Node:  # класс элемента
    def __init__(self, value=None, next_=None):  # инициализируем
        self.value = value   # значением
        self.next = next_  # и ссылкой на следующий элемент

    def __str__(self):
        return "Node value = " + str(self.value)


class LinkedList:  # класс списка
    def __init__(self):  # инициализируем пустым
        self.first = None
        self.last = None

    def clear(self):   # очищаем список
        self.__init__()

    def __str__(self):  # функция печати
        R = ''

        pointer = self.first  # берем первый указатель
        while pointer is not None:  # пока указатель не станет None
            R += str(pointer.value)  # добавляем значение в строку
            pointer = pointer.next  # идем дальше по указателю
            if pointer is not None:  # если он существует добавляем пробел
                R += ' '
        return R

    def pushleft(self, value):  # метод pushleft, который вставляет новый элемент в начало списка.
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def pushright(self, value):  # метод pushright, который добавляет элемент в правую часть списка.
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    def popleft(self):  # Удалить элемент из начала
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохраненный

    def popright(self):  # процедура удаления последнего элемента:
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаем указатель
            while pointer.next is not node:  # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None  # обнуляем указатели, чтобы
            self.last = pointer  # предпоследний стал последним
            return node  # возвращаем сохраненный

# Теперь напишем функционал этого класса, чтобы он стал полноценным итератором.

    def __iter__(self):  # объявляем класс как итератор
        self.current = self.first  # в текущий элемент помещаем первый
        return self  # возвращаем итератор

    def __next__(self):  # метод перехода
        if self.current is None:  # если текущий стал последним
            raise StopIteration  # вызываем исключение
        else:
            node = self.current  # сохраняем текущий элемент
            self.current = self.current.next  # совершаем переход
            return node  # и возвращаем сохраненный
# И в заключение напишем «магический» метод, возвращающий размер структуры данных.

    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count


LL = LinkedList()

LL.pushright(1)
LL.pushleft(2)
LL.pushright(3)
LL.popright()
LL.pushleft(4)
LL.pushright(5)
LL.popleft()

print(LL)
print(len(LL))

print("11. Линейный поиск. Пусть на вход программы поступает массив из произвольного количества "
      "целых чисел и ещё одно целое число, которое будем проверять на вхождение"
      "в этот массив. Задача состоит в том, чтобы вернуть индекс первого вхождения "
      "элемента, если он входит в него, и False если не входит.")


def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False


array = list(map(int, input("Введите последовательность целых чисел:").split()))
element = int(input("Введите число:"))

print(find(array, element))


print("12. Линейный поиск. Напишите функцию count, которая возвращает количество вхождений элемента в массив")


def count(array, element):
    count = 0
    for a in array:
        if a == element:
            count += 1
    return count


array = list(map(int, input("Введите последовательность целых чисел через пробел:").split()))
element = int(input("Введите число:"))

print(count(array, element))

print("13. Бинарный поиск. Пусть на вход программы поступает массив из произвольного количества "
      "целых чисел и ещё одно целое число, которое будем проверять на вхождение"
      "в этот массив. Задача состоит в том, чтобы вернуть индекс первого вхождения "
      "элемента, если он входит в него, и False если не входит.")


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

element = int(input("Введите число от 0 до 98:"))
array = [i for i in range(1, 100)]

print(binary_search(array, element, 0, 99))


  #  import random  модуль, с помощью которого перемешиваем массив
print("14. Наивная сортировка")
# пусть имеем массив всего лишь из 9 элементов
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
is_sort = False   # станет True, если отсортирован
count = 0  # счетчик количества перестановок

while not is_sort:  # пока не отсортирован
    count += 1  # прибавляем 1 к счётчику

    random.shuffle(array)  # перемешиваем массив
    # проверяем, отсортирован ли
    is_sort = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            is_sort = False
            break

print(array)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count)

print("15. Сортировка выбором.")

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    idx_min = i
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:
        array[i],array[idx_min] = array[idx_min], array[i]

print(array)


print("16. Модифицируйте описанный алгоритм для сортировки по убыванию.")

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    idx_max = i
    for j in range(i, len(array)):
        if array[j] > array[idx_max]:
            idx_max = j
    if i != idx_max:
        array[i], array[idx_max] = array[idx_max], array[i]

print(array)


print("17. Сортировка вставками.")

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx - 1] > x:
        array[idx] = array[idx - 1]
        idx -= 1
    array[idx] = x

print(array)


print("18. Сортировка слиянием.")

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]


def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort((L[:middle]))  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы
    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

print(merge_sort(array))


print("19.   Быстрая сортировка.")


def qsort(array, left, right):
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

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

qsort(array, 0, len(array) - 1)
print(array)


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
