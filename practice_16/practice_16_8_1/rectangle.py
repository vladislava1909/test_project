#Итак, у нас есть класс Rectangle с двумя параметрами:
# ширина и высота (a и b). Мы можем найти площадь прямоугольника.
# Для этого нужно длину умножить на высоту (строка кода 6).
# Для решения используем специальный метод get_area.
# Он принимает аргумент self, то есть сам класс Rectangle,
# и возвращает произведение атрибута a (ширина) на b (высота).
import math

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area_rectangle(self):
        return self.a * self.b

# Добавим в нашу программу еще один объект, например Square (квадрат),
# который принимает в качестве аргумента одну сторону. Добавляем данные в исходный файл rectangle.py:


class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2  # возведение в степень 2 (в квадрат)

# Добавим класс круг и метод получения площади круга.


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        return math.pi * self.r ** 2


