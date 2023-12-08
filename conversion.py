import random
from tkinter import Label, ttk, Text, Toplevel
from systems import convert_number


def conversion_mode():
    
    # Create a Toplevel window instead of a new Tk() window
    root = Toplevel()
    root.title("Number Systems - Conversion Mode")
    root.geometry("500x300")

    label = Label(root, text="Enter a number") 
    label.place(x=40, y=30);    
    number_entry = ttk.Entry(root)
    number_entry.place(x=270, y=30)

    label = Label(root, text="Enter the current number system") 
    label.place(x=40, y=60); 
    from_base_entry = ttk.Entry(root)
    from_base_entry.place(x=270, y=60)

    label = Label(root, text="Enter the target number system") 
    label.place(x=40, y=90); 
    to_base_entry = ttk.Entry(root)
    to_base_entry.place(x=270, y=90)

    result_text = Text(root, width=57, height=5)
    result_text.place(x=20, y=120)

    def convert_and_display():
        number = number_entry.get()
        from_base = int(from_base_entry.get())
        to_base = int(to_base_entry.get())

        converted_number = convert_number(number, from_base, to_base)
        if converted_number != "NULL":
            result_text.delete("1.0", "end")
            result_text.insert("1.0", f"The result: {converted_number}")
        else:
            result_text.delete("1.0", "end")
            result_text.insert("1.0", "Error: incorrect input. The number system should be equal to 2, 8, 10, 16. The number must be float(int) and non-negative")

    convert_button = ttk.Button(root, text="Convert", command=convert_and_display)
    convert_button.place(x=40, y=240)

    root.mainloop()
