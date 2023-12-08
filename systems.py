import random
from tkinter import Tk, Label, ttk, Text, Scrollbar, filedialog, Toplevel


def r_to_decimal(num, r):
    res = 0
    try:
        numeric,decimal = num.split('.')
        for i in range(len(numeric)):
            if numeric[i].isdigit():
                res += int(numeric[i]) * (r ** (len(numeric) - i - 1))
            else:
                res += (ord(numeric[i]) - ord('A') + 10) * (r **(len(numeric) - i - 1))
        for i in range(len(decimal)):
            if decimal[i].isdigit():
                res += int(decimal[i]) * (r ** -(i+1))
            else:
                res += (ord(decimal[i]) - ord('A') + 10) * (r **-(i+1))
    except:
        for i in range(len(num)):
            if num[i].isdigit():
                res += int(num[i]) * (r ** (len(num) - i - 1))
            else:
                res += (ord(num[i]) - ord('A') + 10) * (r **(len(num) - i - 1))
    return res

def decimal_to_r(num, r, decimal_places = 5):
    res = ''
    decimal_part = float('0.' + str(num).split('.')[1])
    num = int(num)
    while num > 0:
        temp = num % r
        if temp < 10:
            res += str(temp)
        else:
            res += chr(ord('A') + temp - 10)
        num //= r
    res = res[::-1]
    res += '.'
    for i in range(decimal_places):
        temp = decimal_part * r
        if temp < 10:
            res += str(int(temp))
        else:
            res += chr(ord('A') + int(temp) - 10)
        decimal_part = float('0.' + str(temp).split('.')[1])

    return res

def convert_number(number, from_base, to_base):
    if ((from_base in [2, 8, 16, 10]) == 0 or (to_base in [2, 8, 16, 10]) == 0): return "NULL"
    # Converting a number to decimal notation
    try:
        number = float(number)
    except ValueError:
        return "NULL"

    if number < 0:
        return "NULL"

    if (from_base == 10):
        first_part = int(number)
        if (to_base == 2): decimal_number = bin(first_part)[2:]
        elif (to_base == 8): decimal_number = oct(first_part)[2:]
        elif (to_base == 16): decimal_number = hex(first_part)[2:]
        length = len(str((number - int(number))))
        second_part = round(number - int(number), length)
        return second_part
    # Convert the number to decimal
    decimal_number = int(number) if number.is_integer() else number

    # Convert the decimal number to the target base
    converted_number = format(decimal_number, 'x' if to_base == 16 else '')
    return converted_number
    
    

def self_testing_mode():
    number_type = input("Выберите тип чисел (int/float): ")
    min_value = float(input("Введите нижнюю границу диапазона значений: "))
    max_value = float(input("Введите верхнюю границу диапазона значений: "))
    count = int(input("Введите количество заданий: "))

    correct_answers = 0
    incorrect_answers = 0

    for _ in range(count):
        if number_type == "int":
            number = random.randint(int(min_value), int(max_value))
        elif number_type == "float":
            number = random.uniform(min_value, max_value)
        else:
            print("Ошибка: неверный тип чисел.")
            return

        from_base = random.choice([2, 8, 10, 16])
        to_base = random.choice([2, 8, 10, 16])
        while(from_base == to_base):
            to_base = random.choice([2, 8, 10, 16])

        print(f"Переведите число {number} из системы счисления {from_base} в систему счисления {to_base}")
        user_answer = input("Ваш ответ: ")

        converted_number = convert_number(number, from_base, to_base)
        if user_answer == converted_number:
            print("Правильно!")
            correct_answers += 1
        else:
            print(f"Неправильно. Правильный ответ: {converted_number}")
            incorrect_answers += 1

    print("Выполнено заданий:", count)
    print("Правильных ответов:", correct_answers)
    print("Неправильных ответов:", incorrect_answers)

def testing_mode():
    count = int(input("Введите количество заданий: "))
    correct_answers = 0
    incorrect_answers = 0

    for _ in range(count):
        number = random.randint(1, 100)
        from_base = random.choice([2, 8, 10, 16])
        to_base = random.choice([2, 8, 10, 16])

        print("Переведите число", number, "из системы счисления", from_base, "в систему счисления", to_base)
        user_answer = input("Ваш ответ: ")

        converted_number = convert_number(number, from_base, to_base)
        if user_answer == converted_number:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Неправильно. Правильный ответ:", converted_number)
            incorrect_answers += 1

    print("Выполнено заданий:", count)
    print("Правильных ответов:", correct_answers)
    print("Неправильных ответов:", incorrect_answers)

if __name__ == "__main__":
    print(convert_number("10", 10, 2))