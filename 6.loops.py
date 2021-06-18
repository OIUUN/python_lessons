#  *** Циклы ***

# Оператор цикла while
# Переводится как "пока"

# бесконечный цикл
# Данный бесконечный цикл в терминале прерывается сочетанием клавиш "ctrl" + "c"
# пока условие True(истина) выполняется печатает слово Hello
# while True:
#     print("Hello")

# g = 10
# while g > 0:
#     # g = g - 1
#     g -= 1
#     print(f"Hello {g}")

# инструкция(команда) прерывания цикла по дополнительному условию
# g = 10
# while g > 0:
#     print(f"Hello {g}")
#     if g == 5:
#         break
#     g -= 1

# самостоятельно цикл континум(continue) посмотреть
j = 0
while j < 17:
    if j == 3:
        print("continue")
        j +=2
        continue
    print("Hello")
    j += 2




# Оператор цикла for

# 1. читает значения из итерируемых объектов по порядку
# 2. значение присваивает в свою переменную
# 3. выполняет блок кода своего тела

my_list = [10, 20, 30, 40, 50]

# for i in my_list:
#     print(i)

# for i in my_list[::-1]:
#     print(i)


# генератор списка

# создание списка чисел  в диапазоне от 10 до 100 с шагом 10
num_list = [num * 2 for num in range(10, 100, 10)]


# print(num_list)



