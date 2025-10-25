# """
# ======================================
# 1. Создай класс Person с методом set_data(self, name, age), который сохраняет имя и возраст в объект.
# Добавь метод get_data(self), который возвращает строку вида "Имя: <name>, Возраст: <age>".
# Создай два объекта и задай им разные значения. Выведи информацию по каждому.
class Person:

    def set_data(self, name: str, age: int | float):
        self.name = name
        self.age = age

    def get_data(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

guy = Person()
lady = Person()
lady.set_data("Maria", 25)
guy.set_data("Ivan", 22)
print(guy.get_data())
print(lady.get_data())
# ======================================
# 2. Добавь в класс Point методы set_coords(x, y) и get_coords().
# Создай объект p, задай координаты (7, 12), а затем получи и выведи их.
# После этого измени координаты на (-3, 5) и снова выведи результат через get_coords().
# ======================================
class Point:
    def set_coords(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

p = Point()
p.set_coords(7, 12)
print(p.get_coords())
p.set_coords(-3, 5)
print((p.get_coords()))
# 3. Используя getattr(), получи ссылку на метод get_coords у объекта Point и вызови его.
# Проверь, что результат совпадает с обычным вызовом p.get_coords().
# ======================================
method = getattr(p, "get_coords")
result = method()
print(result)
print(p.get_coords())
# 4. Создай класс Person, в котором метод __init__() принимает имя и возраст и сохраняет их как атрибуты объекта.
# Добавь метод show_info(), который выводит строку "Имя: <name>, возраст: <age>". Создай объект и вызови метод.
# ======================================
# 5. Добавь в класс Person метод __del__(), который выводит сообщение "Удалён объект: <имя>",
# где <имя> — значение поля name. Создай и удали объект вручную с помощью del.
# ======================================
"""Объединил 4 и 5 задание для удобства"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        return f"Имя : {self.name}, возраст: {self.age}"

    def __del__(self):
        print(f"Объект {self.name} удалён")

man = Person("Володя", 23)
print(man.show_info())
del man
# 6. Создай класс Rectangle с инициализацией по умолчанию: ширина 1, высота 1.
# Добавь метод area(), который возвращает площадь прямоугольника.
# Проверь работу с прямоугольником без аргументов и с заданной шириной и высотой.
# ======================================
class Rectangle:
    def __init__(self, width=1, height=1):
        self.widht = width
        self.height = height

    def area(self):
        return self.widht * self.height

arg1 = Rectangle()
print(arg1.area())
arg2 = Rectangle(5, 7)
print(arg2.area())
# 7. Создай класс Logger, который всегда возвращает один и тот же объект.
# При создании экземпляра в __new__ выводи Создание логгера,
# а при вызове __init__ — Инициализация логгера.
# ======================================
class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Создание логгера")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        print("Инициализация логгера")

logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)
