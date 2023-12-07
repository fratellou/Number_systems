import random
from tkinter import Tk, Label, ttk, Text, Scrollbar, filedialog, Toplevel


def convert_number(number, from_base, to_base):
    #if (number < 0): return NULL
    # Check if the number is a float
    is_float = '.' in str(number)

    # Convert the integer part of the float to the desired base
    decimal_number_int = int(str(number).split('.')[0], from_base)
    converted_number_int = format(decimal_number_int, 'x' if to_base == 16 else '')

    # If the number is a float, convert the fractional part as well
    if is_float:
        decimal_number_frac = int(str(number).split('.')[1], from_base)
        converted_number_frac = format(decimal_number_frac, 'x' if to_base == 16 else '')
        converted_number = f"{converted_number_int}.{converted_number_frac}"
    else:
        converted_number = converted_number_int

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
    print(convert_number(5, 10, 2))