# *** Функции ***

# встроенная функция ввода данных
# data = input("Введите данные: ")

# print(f"Вы ввели вот это - {data}")

# Создание(определение) функции

# 1 вариант. Функция, принимающая данные (обладающая аргументами)
def func_1(arg_1):
    s = arg_1 ** 2
    w = s + 10
    print(f"Результат:{w}")

# Вызов функции
# func_1(1000)

def func_2(a, b, c):
    res = a + b + c
    res *= 1000
    print(res)

# func_2(100, 10, 890)

# аргумент может иметь значение по умолчанию
def func_3(arg_1, arg_2=100):
    print(arg_1 * arg_2)

# func_3(10000, 1000)
# func_3(100000)
# func_3(10 ** 2)

# 2 вариант. Функция возвращающая данные
def func_4(arg_1, arg_2):
    res = arg_1 + arg_2
    return res

# d = func_4(100000, 900000)

def func_5(x, y):
    res_1 = x * y
    res_2 = x / y
    return res_1, res_2, x

# первый способ приема данных
d_1 = func_5(10000000, 10)
# второй способ приема данных
a, b, c = func_5(1000, 10)

# print(d_1)
# print(d_1[0])

# print(a, b, c)
# print(b)


# *** Безымянные функции (лямбда выражения, лямбда функции)

# Особенности:
# - всегда обладают аргументами
# - всегда возвращает результат

# Пример 1. Лямбда внутри генератора списка
my_list = [(lambda arg_1: arg_1.upper())(i) for i in "hello"]

# Пример 2. Словарь лямбда выражений
my_lambdas = {
    "*": lambda arg_1, arg_2: arg_1 * arg_2, 
    "+": lambda w, z: w + z
}

# print(my_lambdas["+"](100000, 900000))
# print(my_lambdas["*"](100000, 900000))


# *** Декоратор ***

# Декоратор - функция, обертывающая другую (таргетную) функцию.

# декортатор
def my_decorator(func_object):
    # функция-обертка
    def wrapper(w):
        # доп функциональность ДО
        print("Before")
        w = w * 2
        # вызов целевой функции
        func_object(w)
        # доп функциональность GJCKT
        print("After")
    
    return wrapper

# новый способ применения декторатора
@my_decorator
# Целевая (таргетная) функция
def target_func(arg_1):
    print("Hello! I am a millionaire :)", arg_1)

# старый способ прменения декоратора
# target_func = my_decorator(target_func)

target_func(1000000)

# 