import random
from systems import *
from tkinter import ttk, Toplevel, messagebox, StringVar

def is_valid_number(value):
    try:
        num = int(value)
        return num >= 0
    except ValueError:
        return False
    
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

def check_answers(entries, tasks):
    correct_answers = 0
    incorrect_answers = 0

    for i, entry in enumerate(entries):
        user_answer = entry.get()
        converted_number = convert_number(tasks[i][0], tasks[i][1], tasks[i][2])

        if user_answer == converted_number:
            correct_answers += 1
        else:
            incorrect_answers += 1

    messagebox.showinfo("Результаты теста", f"Правильных ответов: {correct_answers}\nНеправильных ответов: {incorrect_answers}")

def testing_mode():
    root = Toplevel()
    root.title("Number Systems - Testing Mode")
    root.geometry("400x230")

    min_label = ttk.Label(root, text="Enter the minimum number")
    min_label.place(x=60, y=20)
    min_entry = ttk.Entry(root)
    min_entry.place(x=260, y=15, width=70, height=30)

    max_label = ttk.Label(root, text="Enter the maximum number")
    max_label.place(x=60, y=60)
    max_entry = ttk.Entry(root)
    max_entry.place(x=260, y=55, width=70, height=30)

    tpe = StringVar(value="int")
    int_btn = ttk.Radiobutton(root, text="Int", value="int", variable=tpe)
    int_btn.place(x=120, y=100)

    float_btn = ttk.Radiobutton(root, text="Float", value="float", variable=tpe)
    float_btn.place(x=220, y=100)

    def start_test():

        min_val = min_entry.get()
        max_val = max_entry.get()

        if not is_valid_number(min_val) or not is_valid_number(max_val):
            messagebox.showerror("Error", "Enter valid minimum and maximum numbers (integers, not less than 0).")
            return

        min_val = int(min_val)
        max_val = int(max_val)

        
        root.geometry("400x520")
        count = 10
        tasks = []

        for _ in range(count):
            if tpe.get() == "int":
                number = random.randint(min_val, max_val)
            elif tpe.get() == "float":
                number = round(random.uniform(min_val, max_val), 2)

            from_base = random.choice([2, 8, 10, 16])
            to_base = random.choice([2, 8, 10, 16])

            tasks.append((number, from_base, to_base))

        entries = []
        for i, task in enumerate(tasks):
            task_label = ttk.Label(root, text=f"Convert {task[0]} from base 10 to base {task[2]}")
            task_label.place(x=20, y=20 + i * 40)

            entry = ttk.Entry(root)
            entry.place(x=300, y=15 + i * 40, width=70, height=30)
            entries.append(entry)

        start_button.place_forget()
        min_label.place_forget()
        min_entry.place_forget()
        max_label.place_forget()
        max_entry.place_forget()
        int_btn.place_forget()
        float_btn.place_forget()

        submit_button = ttk.Button(root, text="Submit", command=lambda: check_answers(entries, tasks))
        submit_button.place(x=50, y=430,  width=300, height=60)

    start_button = ttk.Button(root, text="Start Test", command=start_test)
    start_button.place(x=50, y=140, width=300, height=60)

    root.mainloop()