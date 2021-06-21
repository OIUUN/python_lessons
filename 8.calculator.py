# *** Пример. Калькулятор ***

# функция-обработчик
def calculate(n1, n2, op):
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2
    else:
        result = f"Что это такое, сэр?: {op}? :("
    return result

# цикл программы
while True:
    # ввод данных
    cmd = input("Коммандуйте, сэр :) ")
    if cmd == "stop":
        print("buy buy!")
        break
    
    num_1 = int(input("Введите 1 число: "))
    num_2 = int(input("Введите 2 число: "))
    op = input("Введите символ операции: ")
    # обработка данных
    result = calculate(num_1, num_2, op)

    # вывод данных
    print(f"Результат: {result}")