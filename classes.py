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
        self.session_id = session_id  # Теперь добавим метод. Не забываем,
        # что метод принимает на вход self первым аргументом.

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


print("10. Наследование. Чтобы задать родительский класс, надо указать его в скобках при объявлении класса,"
      " как будто это аргумент функции: ")

import datetime


class Parent:  # Класс Родитель
    max_quantity = 100000  # Атрибут родителя

    def __init__(self, name, category, quantity_in_stock):  # Метод родителя
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False  # Метод родителя


class Heir(Parent):  # Класс наследник принимает класс родителя в скобках как аргумент функции
    is_critical = True
    needs_to_be_refreshed = True
    refreshed_frequency = datetime.timedelta(days=1)  # Атрибуты Наследника


eggs = Heir(name="eggs", category="food", quantity_in_stock=5)
print(eggs.max_quantity)  # 100000 Класс наследник принял атрибут класса родителя
print(eggs.is_available())  # True Класс наследник принял метод класса наследника


print("11. Важно! Если мы назовем атрибут или метод так же, как он называется в родительском классе, "
      "он будет переопределен.Рассмотрим на примере:")

#  Что получили:
# Переопределили конструктор класса. Теперь мы используем не родительский,
# а свой, и передаём в него другой набор аргументов.
# Так у нас получился кастомизированный набор атрибутов:
# у родительского класса нет атрибута number_of_views.
# Переопределили значение атрибута type с помощью атрибута класса.
# Теперь при вызове type от экземпляра нашего дочернего класса
# мы получим значение атрибута type нашего класса ItemViewEvent.
# Переопределили работу метода show_description:
# теперь он показывает более специфичное для класса описание.


class EventOriginal:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

    def show_description(self):
        print("This is original event.")  # Оригинальный метод родительского класска


class ItemViewEvent(EventOriginal):
    type = "itemViewEvent"

    def __init__(self, timestamp=0, session_id="", number_of_views=0):
        super().__init__(timestamp, session_id)
        self.timestamp = timestamp
        self.session_id = session_id
        self.number_of_views = number_of_views

    def show_description(self):
        print("This event means someone has browsed an item.")  # Переопределенный метод уже в классе наследнике


if __name__ == "__main__":
    test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct", number_of_views=6)
    test_view_event.show_description()
    print(test_view_event.type)


print("12. функции isinstance. Все просто: вы передаёте в неё объект и тип (класс),"
      "а функция возвращает логическое значение результата проверки. "
      "То есть говорит вам, является ли объект экземпляром указанного класса или нет. ")

print(isinstance("foo", str))  # True

print(isinstance(123, ItemViewEvent))  # False
