import tkinter as tk
from systems import *
from tkinter import *
from tkinter import ttk


class SystemsConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Systems Converter")

        self.create_widgets()

    def create_widgets(self):
        # Instruction Label
        self.instruction_label = tk.Label(self.root, text="Enter a number and its base to convert:")
        self.instruction_label.pack()

        # Entry Widget for Number
        self.number_entry = tk.Entry(self.root)
        self.number_entry.pack()

        # Entry Widget for From Base
        self.from_base_entry = tk.Entry(self.root)
        self.from_base_entry.pack()

        # Entry Widget for To Base
        self.to_base_entry = tk.Entry(self.root)
        self.to_base_entry.pack()

        # Output Label
        self.output_label = tk.Label(self.root, text="")
        self.output_label.pack()

        # Convert Button
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_number)
        self.convert_button.pack()

    def convert_number(self):
        number = self.number_entry.get()
        from_base = int(self.from_base_entry.get())
        to_base = int(self.to_base_entry.get())

        converted_number = convert_number(number, from_base, to_base)
        if converted_number is not None:
            self.output_label.config(text=f"Converted Number: {converted_number}")
        else:
            self.output_label.config(text="Error: Invalid number or base.")

def move_btn(btn):
    '''Функция двигает кнопку в левый верхний угол. '''
    btn.grid(row=0, column=0)

if __name__ == "__main__":
    root = tk.Tk()
    btn = Button(text='Бегающая кнопка')
    btn.bind('<Enter>', lambda x: move_btn(btn))
    btn.pack()
    root.mainloop()