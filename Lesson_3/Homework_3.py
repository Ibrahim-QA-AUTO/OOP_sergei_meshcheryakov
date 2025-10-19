# """
# ======================================
# 1. Создай класс Circle, в котором:
# есть атрибуты класса MIN_RADIUS = 1 и MAX_RADIUS = 1000,
# метод класса is_valid_radius(cls, r), который проверяет, входит ли значение в допустимый диапазон.
# Проверь результат вызова:
# print(Circle.is_valid_radius(500))   # True
# print(Circle.is_valid_radius(1500))  # False
# ======================================
class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS
print(Circle.is_valid_radius(500))   # True
print(Circle.is_valid_radius(1500))  # False

# 2. Добавь в класс Circle:
# статический метод area(radius),
# который возвращает площадь круга по формуле π * r ** 2 (используй импорт math.pi),
# инициализацию в __init__, которая сохраняет радиус,
# только если он проходит валидацию через метод is_valid_radius()
# (подумай как можно проверить значения перед тем как записать их в переменные экземпляра класса)
# Пример:
# c = Circle(10)
# print(c.area(c.radius))  # Площадь круга
# ======================================
class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        import math
        return math.pi * radius ** 2

    def __init__(self, radius):
        if self.is_valid_radius(radius):
            self.radius = radius
        else:
            raise ValueError(f"Недопустимое значение для радиуса")

c = Circle(10)
print(c.area(c.radius))
# b = Circle(1001)
# print(b.area(b.radius))

# 3. Расширь Circle, добавив обычный метод print_info, который выводит:
# Радиус: ...
# Допустимый диапазон: [MIN, MAX]
# Метод должен использовать и self, и атрибуты класса через type(self).

class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    def print_info(self):
        print(f"Радиус: {self.radius}")
        print(f"Допустимый диапазон: [{self.MIN_RADIUS}, {self.MAX_RADIUS}]")

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        import math
        return math.pi * radius ** 2

    def __init__(self, radius):
        if self.is_valid_radius(radius):
            self.radius = radius
        else:
            raise ValueError(f"Недопустимое значение для радиуса")

g = Circle(500)
g.print_info()
# Пример вызова:
# c.print_info()
# ======================================
# 4. Создай класс User, в котором:
#
# приватные атрибуты __login и __password;
# метод set_credentials(login, password), который сохраняет их только если оба значения — строки;
# метод get_credentials(), который возвращает кортеж из логина и пароля.
# Попробуй создать объект и изменить логин снаружи напрямую. Проверь, что это не сработает.
# ======================================
class User:

    def __init__(self, login: str='', password: str=''):
        self.__login = login
        self.__password = password

    def set_credentials(self, login: str, password: str):
        if isinstance(login, str) and isinstance(password, str):
            self.__login = login
            self.__password = password
        else:
            raise ValueError(f"Ошибка, логин и пароль должны быть строками")

    def get_credentials(self):
        return (self.__login, self.__password)

a = User("Логин", "Пароль")
print(a.get_credentials())
a.set_credentials("пользователь", "1234")
print(a.get_credentials())
a.__login = "hacker"
print(a.get_credentials())
# a.set_credentials(1234, 444)


# 5. Добавь в User:
#
# метод check_password(password) — возвращает True,
# если переданное значение совпадает с сохранённым паролем;
# приватный метод __encrypt_password(password),
# который возвращает пароль в верхнем регистре (имитация шифрования);
# в set_credentials вызывай __encrypt_password.
# Пример:
# u = User()
# u.set_credentials("daniil", "qwerty")
# print(u.check_password("qwerty"))      # True
# print(u.check_password("qwe"))         # False
class User:
    def __init__(self, login: str = '', password: str = ''):
        self.__login = login
        self.__password = self.__encrypt_password(password)

    def __encrypt_password(self, password: str):
        return password.upper()  # имитация шифрования

    def set_credentials(self, login: str, password: str):
        if isinstance(login, str) and isinstance(password, str):
            self.__login = login
            self.__password = self.__encrypt_password(password)
        else:
            raise ValueError("Ошибка: логин и пароль должны быть строками")

    def check_password(self, password: str):
        return self.__encrypt_password(password) == self.__password

    def get_credentials(self):
        return (self.__login, self.__password)


u = User()
u.set_credentials("daniil", "qwerty")
print(u.check_password("qwerty"))      # True
print(u.check_password("qwe"))         # False
print(u.get_credentials())

# ======================================
# 6. Убедись, что приватный метод __encrypt_password нельзя вызвать извне.
# Попробуй это сделать — и поясни результат.
# Также выведи напрямую u.__password — и проверь, что будет ошибка.
#
# Попробуй добраться до данных через u._User__password
u.__encrypt_password("test") # питон не видит у нашего класса этот метод, потому что он приватный
print(u.__password)
