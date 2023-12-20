from tkinter import Label, ttk, Text, Scrollbar, filedialog, Toplevel, StringVar


class train():
    # displays a tooltip when the mouse hovers over a specific interface element
    def display_tooltip(event, tooltip_label, tooltip):
        tooltip_label.config(text=tooltip)

    # displays information about the translation of numeric systems
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

    # function opens the training mode window of the program
    def training_mode():
        global info_text  
        root = Toplevel()
        root.title("Number Systems - Training Mode")
        root.geometry("1060x600")
        root.configure(background="#c7c7c7")
        
        radio_style = ttk.Style()                    
        radio_style.configure('TRadiobutton',   
            font="Courier 14",   
            foreground="#404040",  
            padding=10,            
            background="#c7c7c7")
        
        radio_style.map('TRadiobutton', foreground=[('hover', '#404040')], background=[('hover', '#c7c7c7')])

        lang = StringVar(value=0)
        ru_btn = ttk.Radiobutton(root, text="Ru", value=1, variable=lang, style='TRadiobutton')
        ru_btn.place(x=820, y=470)

        eng_btn = ttk.Radiobutton(root, text="Eng", value=0, variable=lang, style='TRadiobutton')
        eng_btn.place(x=820, y=500)

        btn_to = ttk.Button(root, text="To another system", command=lambda: train.show_translation_info("to", lang.get()))
        btn_to.place(x=700, y=70, width=300, height=60)
        btn_to.bind("<Enter>", lambda event: train.display_tooltip(event, tooltip_label, "Explanation of the translation into the number system. Select the file to which you want to transfer"))
        btn_to.bind("<Leave>", lambda event: tooltip_label.config(text=""))
    
        btn_from = ttk.Button(root, text="From another system", command=lambda: train.show_translation_info("from", lang.get()))
        btn_from.place(x=700, y=140, width=300, height=60)
        btn_from.bind("<Enter>", lambda event: train.display_tooltip(event, tooltip_label, "Explanation of the transfer to another number system. Select the file from which the translation takes place"))
        btn_from.bind("<Leave>", lambda event: tooltip_label.config(text=""))

        tooltip_label = Label(root, background="#ededed", font="Courier 12", foreground="#404040", height=10, width=35,  wraplength=300)
        tooltip_label.place(x=680, y=240)

        info_text = Text(root, wrap="word", width=57, height=23,  font="Courier 14", foreground="#404040", background="#ededed")
        info_text.place(x=20, y=30)

        scrollbar = Scrollbar(root, command=info_text.yview)
        scrollbar.pack(side="right", fill="y")
        info_text.config(yscrollcommand=scrollbar.set)

        root.mainloop()
