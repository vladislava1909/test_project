print("1. Создание пустого класса.")

class NameClass:
    pass  # этот класс ничего не делает

print("2. Добавление экземпляров в класс.")

class User:
    pass

peter = User()
peter.name = "Peter Robertson"

julia = User()
julia.name = "Julia Donaldson"

print(peter.name)
print(julia.name)


print("3.  Задавать атрибуты, которые будут доступны из любого объекта,"
      " причём без дополнительных действий. "
      "Для этого их надо объявлять прямо внутри класса:")

class User:
    number_of_fingers = 5
    number_of_eyes = 2

lancelot = User()
print(lancelot.number_of_fingers)


print("4. Конструктор класса — «магический» метод __init__, "
      "который заранее определяет атрибуты новых экземпляров."
      " Первым аргументом он обязательно принимает на вход self, "
      "а дальше — произвольный набор аргументов, как обычная функция:")

class UserInit:
    def __init__(self, name, email):
        self.name = name
        self.email = email


print("5. После того, как мы задали конструктор, "
      "при создании объектов в скобки вызова класса можно передавать аргументы,"
      " которые он принимает на вход. Чтобы не запутаться, можно явно указать, "
      "в какой аргумент что класть:")

peter = UserInit(name="Peter Robertson", email="peterrobertson@mail.com")
julia = UserInit(name="Julia Donaldson", email="juliadonaldson@mail.com")

print(peter.name)
print(julia.email)


print("6. __init__, и is_available — это методы. "
      "По умолчанию первым аргументом во все методы класса подается self "
      "— именно так метод получает доступ к экземпляру класса. "
      "При этом, чтобы вызвать исполнение метода, передавать self уже не нужно:")

class Product:
    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False


print("7. Чтобы вызвать исполнение метода, передавать self уже не нужно:")

eggs = Product("eggs", "food", 5)
print(eggs.is_available())


print("8. Пусть мы хотим обрабатывать некоторые события "
      "из уже известных нам логов событий. "
      "Создадим класс с конструктором: "
      "Поправим объявление нашего класса и зададим для каждой "
      "переменной её значение по умолчанию, "
      "чтобы мы могли инициализировать объект без заполнения."
      " Это делается с помощью указания значений по умолчанию "
      "сразу после названия аргумента:")

events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]

class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id  # теперь добавим метод. Не забываем, что метод принимает на вход self первым аргументом.

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")


print("9. После этого мы скрыли реализацию логики от пользователя"
      " — то есть нам уже неважно, как это работает, мы знаем, "
      "что можем подать на вход словарь с нужными ключами,"
      " и всё будет работать само. ")

for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    print(event_obj.timestamp)


