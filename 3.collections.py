# *** Коллекции (контейнеры) ***

# ** Список (list) **

# Создание пустого списка
my_list = []
my_list = list()

# PEP8

# добавление объекта (элемента) в список
my_list.append(100)
my_list.append(3.14)
my_list.append("hello")
my_list.append([10, 20, 30])

# print(my_list)

# Чтение значений элемента
# прямая индексация
# в квадратные скобочки указываем индекс
el = my_list[3]
el = my_list[3][1]

# обратная индексация
el = my_list[-1]

# Замена значения элемента
my_list[0] = 2000

# Удаление элемента по значению
# my_list.remove(3.14)

# Удаление элемента по индексу
del my_list[-2]


# Срез списка
s = "Hello, world!"
my_list = list(s)

my_slice = my_list[2:-5]

print(my_list)
print(my_slice)