import random
from systems import *
from tkinter import ttk, Toplevel, messagebox, Scrollbar

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
    root.geometry("550x500")

    label = ttk.Label(root, text="Enter the number of tasks")
    label.place(x=40, y=30)
    count_entry = ttk.Entry(root)
    count_entry.place(x=270, y=30)

    def start_test():
        count = count_entry.get()
        
        try:
            count = int(count) 
        except ValueError:
            messagebox.showerror("Error", "Input correct number.")
            return
        
        try:
            int(count) < 0 
        except ValueError:
            messagebox.showerror("Error", "Input correct number.")
            return

        tasks = []

        for _ in range(count):
            number = random.randint(1, 100)
            from_base = random.choice([2, 8, 10, 16])
            to_base = random.choice([2, 8, 10, 16])

            tasks.append((number, from_base, to_base))

        entries = []
        for i, task in enumerate(tasks):
            task_label = ttk.Label(root, text=f"Task {i + 1}: Convert {task[0]} from base {task[1]} to base {task[2]}")
            task_label.place(x=20, y=150 + i * 30)

            entry = ttk.Entry(root)
            entry.place(x=350, y=150 + i * 30)
            entries.append(entry)
        
        start_button.place_forget()

        submit_button = ttk.Button(root, text="Submit", command=lambda: check_answers(entries, tasks))
        submit_button.place(x=100, y=70,  width=300, height=60)
        
        
    start_button = ttk.Button(root, text="Start Test", command=start_test)
    start_button.place(x=100, y=70, width=300, height=60)
        # Очистка полей ввода и заданий
        count_entry.delete(0, "end")
        for entry in entries:
            entry.delete(0, "end")


    root.mainloop()