from tkinter import Label, ttk, Text, Scrollbar, filedialog, Toplevel, StringVar


def display_tooltip(event, tooltip_label, tooltip):
    tooltip_label.config(text=tooltip)

def show_translation_info(direction, lang):
    if lang == "1":
        initial_dir = "train/to/ru" if direction == "to" else "train/from/ru"
    else:
        initial_dir = "train/to/eng" if direction == "to" else "train/from/eng"

    filepath = filedialog.askopenfilename(initialdir=initial_dir)
    if filepath != "":
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()
            info_text.delete("1.0", "end")
            info_text.insert("1.0", text)

def training_mode():
    global info_text  
    root = Toplevel()
    root.title("Number Systems - Training Mode")
    root.geometry("1024x600")
        
    lang =  StringVar(value=0)
    ru_btn = ttk.Radiobutton(root, text="Ru", value=1, variable=lang)
    ru_btn.place(x=820, y = 410)

    eng_btn = ttk.Radiobutton(root, text="Eng", value=0, variable=lang)
    eng_btn.place(x=820, y = 430)

    btn_to = ttk.Button(root, text="Translation to another system", command=lambda: show_translation_info("to", lang.get()))
    btn_to.place(x=700, y=70, width=300, height=60)
    btn_to.bind("<Enter>", lambda event: display_tooltip(event, tooltip_label, "Explanation of the\n translation into the number system.\nSelect the file to\n which you want to transfer"))
    btn_to.bind("<Leave>", lambda event: tooltip_label.config(text=""))
 
    btn_from = ttk.Button(root, text="Translation from another system", command=lambda: show_translation_info("from", lang.get()))
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