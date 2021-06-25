# *** Основы объекто-ориентированного программировния ***

# Объект принадлежит определенному классу (типу)
# Объекты обладают свойствами и методами (функции)

# Класс - это некий "чертеж" ("план") объектов.

# Объект определенного класса назывется экземпляром класса.


# Создание (опеределенного) класса
#  Названия классов принято писать с заглавной буквы
class Laika:
    def __init__(self):
        # метод-конструктор
        # здесь создаются свойства (атрибуты, поле)

        self.age = None
    
    def gav(self):
        # метод
        print(f"Гав-гав! Мой вес: {self.age}")

# создание экземпляров (объектов) класса Laika
tuzik = Laika()

# присвоение значения свойству
tuzik.age = 5

# чтение значения из свойства
val = tuzik.age

# print(val)

# вызов метода
# tuzik.gav()

# еще один экземпляр класса Laika
sharik = Laika()

sharik.age = 10

# sharik.gav()


# *** Принцип Наследования ***

# классы могут наследовать свойства и методы у других классов

# создание родительского (предкового) класса
class Cat:
    def __init__(self, n_legs):
        self.num_legs = n_legs

    def move(self):
        print(f"I move. Num_legs: {self.num_legs}")

# создание дочерних классов
class Cat_1(Cat):
        pass

class Cat_2(Cat):
    def info(self):
        print("I am Cat_2")

murka = Cat_1(4)

murka.move()

juchka = Cat_2(6)

juchka.move()
juchka.info()