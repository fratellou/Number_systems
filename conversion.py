from tkinter import Label, ttk, Text, Toplevel, messagebox
from systems import convert_number


def conversion_mode():
    
    root = Toplevel()
    root.title("Number Systems - Conversion Mode")
    root.geometry("500x350")
    root.configure(background="#78ba91")

    label = Label(root, text="Enter a number") 
    label.place(x=20, y=30);    
    number_entry = ttk.Entry(root)
    number_entry.place(x=250, y=25, width=70, height=30)

    label = Label(root, text="Enter the current number system") 
    label.place(x=20, y=70); 
    from_base_entry = ttk.Entry(root)
    from_base_entry.place(x=250, y=65, width=70, height=30)

    label = Label(root, text="Enter the target number system") 
    label.place(x=20, y=110); 
    to_base_entry = ttk.Entry(root)
    to_base_entry.place(x=250, y=105, width=70, height=30)

    result_text = Text(root, width=57, height=5)
    result_text.place(x=20, y=150)

    def convert_and_display():
        number = number_entry.get()
        from_base = int(from_base_entry.get())
        to_base = int(to_base_entry.get())

        converted_number = convert_number(number, from_base, to_base)
        if converted_number != "NULL":
            result_text.delete("1.0", "end")
            result_text.insert("1.0", f"The result: {converted_number}")
        else:
            messagebox.showerror("Error", "The number system should be equal to 2, 8, 10, 16. The number must be float(int) and non-negative")
            return

    convert_button = ttk.Button(root, text="Convert", command=convert_and_display)
    convert_button.place(x=100, y=260, width=300, height=60)

    root.mainloop()
