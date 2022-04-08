print("Создадим конструктор, который будет описывать прямоугольник с имеющимися характеристиками: ширина и высота."
      "Вычислим площадь фигуры (area):")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def GetWidh(self):
        return self.width  # Метод возвращает ширину

    def GetHeight(self):
        return self.height  # Метод возвращает высоту

    def GetArea(self):
        return self.width * self.height
