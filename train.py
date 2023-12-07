from tkinter import Label, ttk, Text, Scrollbar, filedialog, Toplevel

def display_tooltip(event, tooltip_label, tooltip):
    tooltip_label.config(text=tooltip)

def show_translation_info(direction):
    initial_dir = "to" if direction == "to" else "from"
    
    filepath = filedialog.askopenfilename(initialdir=initial_dir)
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            info_text.delete("1.0", "end")
            info_text.insert("1.0", text)

def training_mode():
    global info_text  

    root = Toplevel()
    root.title("Number Systems - Training Mode")
    root.geometry("1024x600")

    btn_to = ttk.Button(root, text="Translation to another system", command=lambda: show_translation_info("to"))
    btn_to.place(x=700, y=70, width=300, height=60)
    btn_to.bind("<Enter>", lambda event: display_tooltip(event, tooltip_label, "Explanation of the\n translation into the number system.\nSelect the file to\n which you want to transfer"))
    btn_to.bind("<Leave>", lambda event: tooltip_label.config(text=""))
 
    btn_from = ttk.Button(root, text="Translation from another system", command=lambda: show_translation_info("from"))
    btn_from.place(x=700, y=140, width=300, height=60)
    btn_from.bind("<Enter>", lambda event: display_tooltip(event, tooltip_label, "Explanation of the\n transfer to another number system.\nSelect the file from\n which the translation takes place"))
    btn_from.bind("<Leave>", lambda event: tooltip_label.config(text=""))

    tooltip_label = Label(root)
    tooltip_label.place(x=720, y=300)

    info_text = Text(root, wrap="word", width=80, height=30)
    info_text.place(x=20, y=30)

    scrollbar = Scrollbar(root, command=info_text.yview)
    scrollbar.pack(side="right", fill="y")
    info_text.config(yscrollcommand=scrollbar.set)

    root.mainloop()