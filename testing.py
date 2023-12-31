import random
from systems import *
from tkinter import ttk, Toplevel, messagebox, StringVar, Text

class testing():
    # It tries to convert the value to an integer and returns `True` if the conversion was successful and the value is greater than or equal to zero, otherwise it returns `False'.
    def is_valid_number(value):
        try:
            num = int(value)
            return num >= 0
        except ValueError:
            return False

    # function creates a self-test window
    def self_testing_mode():
        root = Toplevel()
        root.title("Number Systems - Self-Test Mode")
        root.geometry("400x240")
        root.configure(background="#c7c7c7")

        label = ttk.Label(root)
        label.place(width=400, heigh=105)

        entry_style = ttk.Style()                    
        entry_style.configure('TEntry',   
            font="Courier 14",   
            foreground="#404040",
            fieldbackground="#c7c7c7") 
        
        min_label = ttk.Label(root, text="Enter the minimum number")
        min_label.place(x=10, y=10)
        min_entry = ttk.Entry(root, font="Courier 14", style="TEntry")
        min_entry.place(x=300, y=17, width=70, height=30)

        max_label = ttk.Label(root, text="Enter the maximum number")
        max_label.place(x=10, y=50)
        max_entry = ttk.Entry(root, font="Courier 14", style="TEntry")
        max_entry.place(x=300, y=57, width=70, height=30)


        radio_style = ttk.Style()                    
        radio_style.configure('TRadiobutton',   
            font="Courier 14",   
            foreground="#404040",  
            padding=10,            
            background="#c7c7c7")  
        
        radio_style.map('TRadiobutton', foreground=[('hover', '#404040')], background=[('hover', '#c7c7c7')])

        tpe = StringVar(value="int")
        int_btn = ttk.Radiobutton(root, text="Int", value="int", variable=tpe, style = 'TRadiobutton')
        int_btn.place(x=120, y=110)

        float_btn = ttk.Radiobutton(root, text="Float", value="float", variable=tpe, style = 'TRadiobutton')
        float_btn.place(x=220, y=110)

        # function is an event handler for the test start button. It reads the values from the minimum and maximum number input fields, checks them for validity, creates a task for the test and displays it in the window.
        def start_test():

            min_val = min_entry.get()
            max_val = max_entry.get()

            if not testing.is_valid_number(min_val) or not testing.is_valid_number(max_val):
                messagebox.showerror("Error", "Enter valid minimum and maximum numbers (integers, not less than 0).")
                return


            result_text = Text(root, width=39, height=5,  font="Courier 14", foreground="#404040", background="#ededed")
            result_text.place(x=10, y=130)

            root.geometry("430x280")
            label = ttk.Label(root)
            label.place(width=900, heigh=105)

            start_button.place_forget()
            min_label.place_forget()
            min_entry.place_forget()
            max_label.place_forget()
            max_entry.place_forget()
            int_btn.place_forget()
            float_btn.place_forget()

            min_val = int(min_val)
            max_val = int(max_val)
            tasks = []

            if tpe.get() == "int":
                number = random.randint(min_val, max_val)
            elif tpe.get() == "float":
                number = round(random.uniform(min_val, max_val), 2)

            from_base = random.choice([2, 8, 10, 16])
            to_base = random.choice([2, 8, 10, 16])
            while from_base == to_base:
                to_base = random.choice([2, 8, 10, 16])
            number = systems.convert_number(str(number), 10, int(from_base))
            tasks.append((str(number), from_base, to_base))

            root.geometry("455x350")

            entries = []
            for i, task in enumerate(tasks):
                task_label = ttk.Label(root, text=f"Convert {task[0]} from base {task[1]} to base {task[2]}")
                task_label.place(x=10, y=10 + i * 40)

                entry = ttk.Entry(root, font="Courier 14", style="TEntry")
                entry.place(x=220, y=57 + i * 40, width=70, height=30)
                entries.append(entry)
            
            task_label = ttk.Label(root, text="Enter the answer")
            task_label.place(x=10, y=50)

            # the event handler for the response verification button
            def answer(entries, tasks):           
                user_answer = entry.get()
                converted_number = systems.convert_number(tasks[i][0], tasks[i][1], tasks[i][2])

                if user_answer == converted_number:
                    result_text.delete("1.0", "end")
                    result_text.insert("1.0", f"Correct!")
                else:
                    result_text.delete("1.0", "end")
                    result_text.insert("1.0", f"Incorrect. Correct answer: {converted_number}")


            submit_button = ttk.Button(root, text="Submit", command=lambda: answer(entries, tasks))
            submit_button.place(x=80, y=270,  width=300, height=60)

        start_button = ttk.Button(root, text="Start Test", command=start_test)
        start_button.place(x=50, y=150, width=300, height=60)
        
        root.mainloop()

    def check_answers(entries, tasks):
        correct_answers = 0
        incorrect_answers = 0

        for i, entry in enumerate(entries):
            user_answer = entry.get()
            converted_number = systems.convert_number(tasks[i][0], tasks[i][1], tasks[i][2])

            if user_answer == converted_number:
                correct_answers += 1
            else:
                incorrect_answers += 1

        messagebox.showinfo("Test result", f"Correct answers: {correct_answers}\nIncorrect answers: {incorrect_answers}")

    # function creates a new windo
    def testing_mode():
        root = Toplevel()
        root.title("Number Systems - Testing Mode")
        root.geometry("400x240")
        root.configure(background="#c7c7c7")

        label = ttk.Label(root)
        label.place(width=400, heigh=105)

        entry_style = ttk.Style()                    
        entry_style.configure('TEntry',   
            font="Courier 14",   
            foreground="#404040",
            fieldbackground="#c7c7c7") 
        
        min_label = ttk.Label(root, text="Enter the minimum number")
        min_label.place(x=10, y=10)
        min_entry = ttk.Entry(root, font="Courier 14", style="TEntry")
        min_entry.place(x=300, y=17, width=70, height=30)

        max_label = ttk.Label(root, text="Enter the maximum number")
        max_label.place(x=10, y=50)
        max_entry = ttk.Entry(root, font="Courier 14", style="TEntry")
        max_entry.place(x=300, y=57, width=70, height=30)


        radio_style = ttk.Style()                    
        radio_style.configure('TRadiobutton',   
            font="Courier 14",   
            foreground="#404040",  
            padding=10,            
            background="#c7c7c7")  
        
        radio_style.map('TRadiobutton', foreground=[('hover', '#404040')], background=[('hover', '#c7c7c7')])

        tpe = StringVar(value="int")
        int_btn = ttk.Radiobutton(root, text="Int", value="int", variable=tpe, style = 'TRadiobutton')
        int_btn.place(x=120, y=110)

        float_btn = ttk.Radiobutton(root, text="Float", value="float", variable=tpe, style = 'TRadiobutton')
        float_btn.place(x=220, y=110)

        def start_test():

            min_val = min_entry.get()
            max_val = max_entry.get()

            if not testing.is_valid_number(min_val) or not testing.is_valid_number(max_val):
                messagebox.showerror("Error", "Enter valid minimum and maximum numbers (integers, not less than 0).")
                return

            min_val = int(min_val)
            max_val = int(max_val)

            
            root.geometry("570x520")
            count = 10
            tasks = []

            label = ttk.Label(root)
            label.place(width=570, heigh=420)

            for _ in range(count):
                if tpe.get() == "int":
                    number = random.randint(min_val, max_val)
                elif tpe.get() == "float":
                    number = round(random.uniform(min_val, max_val), 2)

                from_base = random.choice([2, 8, 10, 16])
                to_base = random.choice([2, 8, 10, 16])
                while from_base == to_base:
                    to_base = random.choice([2, 8, 10, 16])
                number = systems.convert_number(str(number), 10, int(from_base))
                tasks.append((str(number), from_base, to_base))

            entries = []
            for i, task in enumerate(tasks):
                task_label = ttk.Label(root, text=f"Convert {task[0]} from base {task[1]} to base {task[2]}")
                task_label.place(x=10, y=10 + i * 40)

                entry = ttk.Entry(root, font="Courier 14", style="TEntry")
                entry.place(x=480, y=15 + i * 40, width=70, height=30)
                entries.append(entry)

            start_button.place_forget()
            min_label.place_forget()
            min_entry.place_forget()
            max_label.place_forget()
            max_entry.place_forget()
            int_btn.place_forget()
            float_btn.place_forget()

            submit_button = ttk.Button(root, text="Submit", command=lambda: testing.check_answers(entries, tasks))
            submit_button.place(x=140, y=440,  width=300, height=60)

        start_button = ttk.Button(root, text="Start Test", command=start_test)
        start_button.place(x=50, y=150, width=300, height=60)

        root.mainloop()