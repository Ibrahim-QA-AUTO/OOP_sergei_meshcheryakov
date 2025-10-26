# """
# ======================================
# 1. Создай класс SecureData, который:
#
# имеет атрибут __secret, задаваемый в __init__;
# переопределяет __getattribute__, чтобы при попытке получить __secret извне выбрасывать ValueError;
# внутри класса доступ к __secret должен работать.
# Проверь:
# data = SecureData("пароль123")
# print(data.__secret)      # ошибка
# print(data.get_secret())  # "пароль123"
class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def __getattribute__(self, name):
        if name in ("__secret", "_SecureData__secret"):
            raise ValueError(f"Доступ к атрибуту '{name}' извне запрещен")
        return object.__getattribute__(self, name)

    def get_secret(self):
        return object.__getattribute__(self, "_SecureData__secret")


data = SecureData("пароль123")

# print(data.get_secret())
# print(data.__secret)

class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def __getattribute__(self, name):
        if name in ("__secret", "_SecureData__secret"):
            raise ValueError(f"Доступ к атрибуту '{name}' извне запрещен")
        return object.__getattribute__(self, name)

    def get_secret(self):
        return object.__getattribute__(self, "_SecureData__secret")

    def __setattr__(self, key, value):
        if key == "token":
            raise AttributeError(f"Запрещено создавать атрибут с именем 'token'")
        object.__setattr__(self, key, value)


data = SecureData("пароль123")

# data.token = "abc123"  # ❌ AttributeError
# data.other = "ok"      # ✅ работает
# print(data.other)      # ok


# ======================================
# 3. Создай класс SafeDict, в котором:
#
# нет атрибута default;
# реализован __getattr__, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
# реализован __delattr__, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
# Проверь:
# d = SafeDict()
# print(d.unknown)     # "N/A"
# d.key = 10
# del d.key            # "Удалён атрибут key"
class SafeDict:

    def __getattr__(self, name):
        return "N/A"

    def __delattr__(self, name):
        print(f"Удален атрибут {name}")

d = SafeDict()
print(d.unknown)     # "N/A"
d.key = 10
del d.key            # "Удалён атрибут key"
# ======================================
# 4. Создай класс Employee с приватными полями __name и __salary.
# Добавь @property для поля salary, а также сеттер с валидацией:
#
# зарплата должна быть положительным числом;
# если нет — выбрасывать ValueError.
# Проверь, что:
# e = Employee("Daniil", 5000)
# print(e.salary)   # 5000
# e.salary = 8000
# print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError

class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value: int | float):
        if value < 0:
            raise ValueError("Зарплата не может быть меньше 0")
        self.__salary = value

e = Employee("Daniil", 5000)
print(e.salary)   # 5000
e.salary = 8000
print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError

# ======================================
# 5. Добавь @deleter для поля salary, чтобы при удалении выводилось "зарплата удалена"
# и поле реально исчезало.
# Проверь:
#
# del e.salary
# print(e.__dict__)  # salary нет
class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value: int | float):
        if value < 0:
            raise ValueError("Зарплата не может быть меньше 0")
        self.__salary = value

    @salary.deleter
    def salary(self):
        del self.__salary

e = Employee("Daniil", 5000)
del e.salary
print(e.__dict__)  # salary нет
# 6. Представь, что ты пишешь обёртку над HTML-формой.
# Создай класс LoginForm с полем username, которое реализовано через @property.
#
# Логика:
# геттер возвращает self._username
# сеттер добавляет лог "username изменён"
# Проверь, что:
# form = LoginForm()
# form.username = "admin"  # выводит лог
# print(form.username)     # "admin"
class LoginForm:

    def __init__(self, username = ''):
        self._username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        print("username изменён")
        self._username = username

form = LoginForm()
form.username = "admin"  # выводит лог
print(form.username)     # "admin"
# ======================================
# 7. Создай класс Card, где:
# поле __number хранит номер карты (строка);
# в @property возвращай номер с маской **** **** **** 1234;
# в @setter проверяй, что номер состоит из 16 цифр;
# в @deleter логируй удаление номера с текущим временем.
# Напиши тесты (через assert)
# проверку установки корректного номера;
# проверку исключения при вводе короткого номера;
# проверку вывода замаскированного номера.
from datetime import datetime

class Card:

    def __init__(self, number = ""):
        self.__number = number

    @property
    def number(self):
        return "**** **** **** " + self.__number[-4:]

    @number.setter
    def number(self, value):
        if not (isinstance(value, int) or isinstance(value, str)):
            raise ValueError("Нужно ввести цифры")
        value = str(value)
        if not (len(value)) == 16:
            raise ValueError("Номер карты должен состоять из 16 цифр")
        if not value.isdigit():
            raise ValueError("Номер карты должен состоять только из цифр")
        self.__number = value

    @number.deleter
    def number(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Номер карты удалён в {now}")
        del self.__number

c = Card()

c.number = "1234567812345678"
assert c.number == "**** **** **** 5678"
print("✅ Корректный номер установлен и геттер возвращает замаскированный номер")

try:
    c.number = "1234"
except ValueError as e:
    assert str(e) == "Номер карты должен состоять из 16 цифр"
    print("✅ Короткий номер вызвал ValueError")

c.number = "8765432187654321"
masked = c.number
assert masked == "**** **** **** 4321"
print("✅ Вывод замаскированного номера работает корректно")
# ======================================
# 8. Создай класс UserData для API регистрации пользователя:
# email — строка, содержит @;
# age — целое число ≥ 18;
# is_active — bool;
# свойство .json возвращает словарь для запроса.
# Напиши тест (через assert)
# проверь, что при age = 15 выбрасывается ValueError;
# проверь, что email без @ вызывает ошибку;
# проверь, что json возвращает корректную структуру.

class UserData:

    def __init__(self, email: str, age: int, is_active: bool):
        if not "@" in email:
            raise ValueError(f"Ошибка! в вашем email: {email} не содержится символ @")
        if age < 18:
            raise ValueError(f"Ошибка! ваш возраст: {age} меньше допустимого")
        self.__email = email
        self.__age = age
        self.__is_active = is_active

    @property
    def json(self):
        return {
            "email": self.__email,
            "age": self.__age,
            "is_active": self.__is_active
        }

# 1️⃣ Проверка возраста < 18
try:
    UserData("a@a.ru", 15, True)
    assert False, "Возраст < 18: ValueError не выброшен"
except ValueError:
    print("✅ Тест 1 пройден: возраст < 18 вызвал ValueError")

# 2️⃣ Проверка email без @
try:
    UserData("aaa.ru", 20, True)
    assert False, "Некорректный email: ValueError не выброшен"
except ValueError:
    print("✅ Тест 2 пройден: некорректный email вызвал ValueError")

# 3️⃣ Проверка свойства .json
user = UserData("user@example.com", 25, True)
assert user.json == {
    "email":"user@example.com",
    "age": 25,
    "is_active": True
}, ".json вернуло неверный результат"
print("✅ Тест 3 пройден: .json возвращает корректную структуру")






# """