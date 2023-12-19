from tkinter import Label, ttk, Text, Toplevel, messagebox
from systems import convert_number

#function checks whether the value of `value` is a valid number. It converts the value to an integer and checks whether it belongs to one of the numeric systems: 2, 8, 10 or 16. 
def valid_number(value):
    try:
        num = int(value)
        num in [2, 8, 10, 16]
        return num >= 0
    except ValueError:
        return False

#it checks each character in the value of `value` and verifies that the characters are valid for a given numeric system. The function also checks that the dot separator characters are not repeated.
def number_system(value, system):
    ans = 1
    value.lower() 
    dot = 0
    if (system == "2"):
        for num in value:
            if (num == '.') & (dot == 1):
                ans = 0
                break
            if num == '.': dot = 1
            if num not in ['0', '1', '.']:
                ans = 0    
                break
    if (system == "8"):
        for num in value:
            if (num == '.') & (dot == 1):
                ans = 0
                break
            if num == '.': dot = 1
            if num not in ['0', '1', '2', '3', '4', '5', '6', '7', '.']:
                ans = 0 
                break
    if (system == "10"):
        for num in value:
            if (num == '.') & (dot == 1):
                ans = 0
                break
            if num == '.': dot = 1
            if num not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                ans = 0 
                break    
    if (system == "16"):
        for num in value:
            if (num == '.') & (dot == 1):
                ans = 0
                break
            if num == '.': dot = 1
            if num not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '.']:
                ans = 0 
                break
    return ans 

#function creates a graphical interface for the conversion mode of numeric systems
def conversion_mode():
    
    root = Toplevel()
    root.title("Number Systems - Conversion Mode")
    root.geometry("500x380")
    root.configure(background="#c7c7c7")

    entry_style = ttk.Style()                    
    entry_style.configure('TEntry',   
        font="Courier 14",   
        foreground="#404040",
        fieldbackground="#c7c7c7") 
    
    label = ttk.Label(root)
    label.place(width=900, heigh=140)

    label = Label(root, text="Enter a number", background="#ededed", font="Courier 14", foreground="#404040") 
    label.place(x=10, y=10);    
    number_entry = ttk.Entry(root, style="TEntry", font="Courier 14")
    number_entry.place(x=370, y=10, width=70, height=30)

    label = Label(root, text="Enter the current number system", background="#ededed", font="Courier 14", foreground="#404040") 
    label.place(x=10, y=50); 
    from_base_entry = ttk.Entry(root, style="TEntry", font="Courier 14")
    from_base_entry.place(x=370, y=50, width=70, height=30)

    label = Label(root, text="Enter the target number system", background="#ededed", font="Courier 14", foreground="#404040") 
    label.place(x=10, y=90); 
    to_base_entry = ttk.Entry(root, style="TEntry", font="Courier 14")
    to_base_entry.place(x=370, y=90, width=70, height=30)

    result_text = Text(root, width=40, height=5, wrap="word", font="Courier 14", foreground="#404040", background="#ededed")
    result_text.place(x=20, y=160)

    # function checks the correctness of the entered values and converts a number from the current numeric system to the target numeric system
    def convert_and_display():

        if not number_system(number_entry.get(), from_base_entry.get()) or not valid_number(from_base_entry.get()) or not valid_number(to_base_entry.get()):
            messagebox.showerror("Error", "The number systems must be equal to 2, 8, 10, 16. The entered number must not be negative and must be in the current number system.")
            return
        
        number = number_entry.get()
        from_base = int(from_base_entry.get())
        to_base = int(to_base_entry.get())

        converted_number = convert_number(number, from_base, to_base)
        if converted_number != "NULL":
            result_text.delete("1.0", "end")
            result_text.insert("1.0", f"The result: {converted_number}")
        else:
            messagebox.showerror("Error", "The number system should be equal to 2, 8, 10, 16. The entered number must not be negative and must be in the current number system.")
            return

    convert_button = ttk.Button(root, text="Convert", command=convert_and_display)
    convert_button.place(x=100, y=300, width=300, height=60)

    root.mainloop()
