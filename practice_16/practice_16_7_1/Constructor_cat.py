print("Откройте сайт «Дом питомца» и на основе имеющихся в нем данных "
      "создайте конструктор класса Cat со следующими параметрами: имя, пол, возраст.")

class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def PrintCat(self):
        print("Имя кота:", self.name, "Пол:", self.gender, "Возраст:", self.age)



