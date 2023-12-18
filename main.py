from systems import *
from train import *
from conversion import *
from testing import *
from tkinter import *
from tkinter import ttk

def display_tooltip(event, tooltip_label, tooltip):
    tooltip_label.config(text=tooltip)

def main():
    root = Tk()
    root.title("Number Systems")
    root.geometry("350x500") 
    root.configure(background="#78ba91")

    label_style = ttk.Style()
    label_style.configure(".",        
                    font="Courier 14",   
                    foreground="#004d1a",  
                    padding=10,            
                    background="#b3dfbc")  

    btn_style = ttk.Style()
    btn_style.configure("TButton", font="Courier 14", foreground="#004d1a", padding=10, background="#b3dfbc")
    btn_style.map("TButton", background=[("active", "#78ba91")])
    btn_style.configure("TButton", relief="flat", focuscolor="#78ba91") 

    btn = ttk.Button(text="Training mode", command=training_mode) 
    btn.place(x=25, y=20, width=300, height=60)  
    btn.bind("<Enter>", lambda event: display_tooltip(event, tooltip_label, "A training mode in which information is provided on how to translate into different number systems"))
    btn.bind("<Leave>",lambda event: (btn.configure(style="TButton"), tooltip_label.config(text="")))

    btn = ttk.Button(text="Conversion mode", command=conversion_mode) 
    btn.place(x=25, y=90, width=300, height=60)   
    btn.bind("<Enter>", lambda event: display_tooltip(event, tooltip_label, "Translation mode, when the program itself translates a number specified by the user from one specified number system to another"))
    btn.bind("<Leave>", lambda event: tooltip_label.config(text=""))

    btn = ttk.Button(text="Self-test mode", command=self_testing_mode) 
    btn.place(x=25, y=160, width=300, height=60)
    btn.bind("<Enter>", lambda event: display_tooltip(event, tooltip_label, "Self-test mode, when the program gives the user a translation task, then checks the correctness of the translation"))
    btn.bind("<Leave>", lambda event: tooltip_label.config(text=""))

    btn = ttk.Button(text="Testing mode", command=testing_mode) 
    btn.place(x=25, y=230, width=300, height=60)   
    btn.bind("<Enter>", lambda event: display_tooltip(event, tooltip_label, "Testing mode, when the program issues translation tasks to the user, then checks the correctness of the translation and gives the final result"))
    btn.bind("<Leave>", lambda event: tooltip_label.config(text=""))   

    tooltip_label = Label(root, background="#b3dfbc", font="Courier 12", foreground="#004d1a", height=10, width=35,  wraplength=300)
    tooltip_label.place(y=320)

    root.mainloop()

if __name__ == "__main__":
    main()