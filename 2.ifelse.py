# *** Логические операции ***

z = 3
w = 2

# операция "равно"
# мы спрашиваем "значение z равно значению w?"
# ответбудет присвоен переменной result
result = z == w

# операция "не равно"
result = z!= w

# операция "меньше"
result = z < w

# операция "больше"
result = z > w

# операция "меньше либо равно"
result = z <= w

# операция "больше либо равно"
result = z >= w

# чистые логические операции

var_1 = True
var_2 = True

# оператор "НЕ" (NOT, инверсия)
result = not var_1

# оператор "И" (AND)
# возвращает True только тогда, когда обе переменных являются True
result = var_1 and var_2

# оператор "ИЛИ" (OR)
# возвращет False только тогда, когда обе переменные являются False
result = var_1 or var_2

#  print(result)


# *** Условные операторы ***

# Оператор "IF" ("если")
# if False:
#     w = "hello"
#     print(w)

# z = 10

# if z < 3: 
#     print("меньше")
# else:
#     print("не меньше")

v = "G"

if v == "B":
    res = "literal B"
elif v == "A":
    res = "literal A"
elif v == "D":
    res = "literal D"
elif v == "W":
    res = "litteral W"
else:
    res = "не понятный мне символ :("

print(res)
