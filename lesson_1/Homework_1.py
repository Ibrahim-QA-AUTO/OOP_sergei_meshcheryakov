# """
# ++++++++++++++++++++++++++++++++++++++
# Классы и атрибуты
# ++++++++++++++++++++++++++++++++++++++
# ======================================
# 1. Создай класс Dog с атрибутами класса species = "canis" и legs = 4.
# Затем создай два объекта этого класса и измени у одного из них локальный атрибут.
# Проверь, как это повлияло на значения у обоих объектов.
# Убедись, что __dict__ объектов отражает изменения.
class Dog:
    species = "canis"
    legs = 4

dog1 = Dog()
dog2 = Dog()
dog1.legs = 3
print(dog1.legs, dog2.legs)
print(dog1.__dict__)
print(dog2.__dict__)
#
# 2. Добавь в класс Dog строку документации, описывающую его назначение.
# Затем выведи её на экран.
# После этого добавь в объект класса новые атрибуты name и age,
# а затем удали name.
# Проверь, что произойдёт при попытке снова вывести объект.name.
class Dog:
    """
    Класс для создания собак, атрибутами являются: порода, количество ног, имя и возраст
    """
    species = "canis"
    legs = 4
    name = "Шарик"
    age = 2
print(Dog.__doc__)
del Dog.name
# print(Dog.name)
# 3. Создай класс User с атрибутами класса role = "guest" и active = True.
# С помощью функций getattr(), setattr(), hasattr() и delattr():
#
# измени значение role на "admin",
# проверь наличие active,
# добавь новый атрибут email,
# удали role.
# Убедись, что всё работает корректно, и выведи итоговое содержимое __dict__ класса User.
class User:
    role = "guest"
    active = True

setattr(User, "role", "admin")
print(getattr(User, "role", "admin"))
print(hasattr(User, "active"))
setattr(User, "email", "123@mail.ru")
print(getattr(User, "email", "123@mail.ru"))
delattr(User,"role")
print(User.__dict__)