from Constructor_cat import Cat

print("В отдельный файл импортируйте и создайте объект Cat, "
      "который выводит имеющихся на сайте котов, с одинаковыми параметрами, "
      "но с разными значениями.  ")

Baron = Cat("Baron", "male", 2)
Sam = Cat("Sam", "male", 2)

Baron.PrintCat()
Sam.PrintCat()