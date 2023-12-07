from systems import *
from train import *
from conversion import *
from tkinter import *
from tkinter import ttk

def display_tooltip(event, tooltip_label, tooltip):
    tooltip_label.config(text=tooltip)

def main():
    root = Tk()
    root.title("Number Systems")
    root.geometry("350x500") 

    btn = ttk.Button(text="Training mode", command=training_mode) 
    btn.place(x=25, y=20, width=300, height=60)  
    btn.bind("<Enter>", lambda event: display_tooltip(event, tooltip_label, "A training mode \nin which information is provided   \non how to translate into\ndifferent number systems"))
    btn.bind("<Leave>", lambda event: tooltip_label.config(text=""))

    btn = ttk.Button(text="Conversion mode", command=conversion_mode) 
    btn.place(x=25, y=90, width=300, height=60)   
    btn.bind("<Enter>", lambda event: display_tooltip(event, tooltip_label, "Translation mode,\nwhen the program itself translates \na number specified by  \nthe user from one specified\nnumber system to another"))
    btn.bind("<Leave>", lambda event: tooltip_label.config(text=""))

    btn = ttk.Button(text="Self-test mode", command=self_testing_mode) 
    btn.place(x=25, y=160, width=300, height=60)
    btn.bind("<Enter>", lambda event: display_tooltip(event, tooltip_label, "Self-test mode,  \nwhen the program gives the user a  \ntranslation task, then \nchecks the correctness of  \nthe translation"))
    btn.bind("<Leave>", lambda event: tooltip_label.config(text=""))

    btn = ttk.Button(text="Testing mode", command=testing_mode) 
    btn.place(x=25, y=230, width=300, height=60)   
    btn.bind("<Enter>", lambda event: display_tooltip(event, tooltip_label, "Testing mode,    \nwhen the program issues translation\ntasks to the user, then\nchecks the correctness of the\n translation and gives\n the final result"))
    btn.bind("<Leave>", lambda event: tooltip_label.config(text=""))   

    tooltip_label = Label(root)
    tooltip_label.place(x=65, y=350)

    root.mainloop()

if __name__ == "__main__":
    main()