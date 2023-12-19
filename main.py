from systems import *
from train import *
from conversion import *
from testing import *
from tkinter import *
from tkinter import ttk, messagebox
import pickle
import hashlib

def display_tooltip(event, tooltip_label, tooltip):
    tooltip_label.config(text=tooltip)

# Hashing the activation key
def hash_activation_key(key):
    hashed_key = hashlib.sha256(key.encode()).hexdigest()
    return hashed_key

# Saving the encrypted key in the database
def save_activation_key(key):
    hashed_key = hash_activation_key(key)

    try:
        # Attempt to download existing keys from a file
        with open("database.bin", "rb") as file:
            keys = pickle.load(file)
    except FileNotFoundError:
        # If the file does not exist, create an empty dataset
        keys = set()

    # Adding a new key
    keys.add(hashed_key)

    # Saving keys back to a file
    with open("database.bin", "wb") as file:
        pickle.dump(keys, file)

# Checking the activation key
def check_key(key):
    hashed_key = hash_activation_key(key)

    try:
        with open("database.bin", "rb") as file:
            keys = pickle.load(file)
    except FileNotFoundError:
        return False

    # Checking the key
    return hashed_key in keys
    
def activation_mode():
    def check():
        key = key_entry.get()
        if check_key(key):
            messagebox.showinfo("Activation", "Activation successful!")
            root.destroy()
            main()
        else:
            messagebox.showerror("Activation", "Invalid key. Please try again.") 
        
    root = Tk()
    root.title("Activation")
    root.geometry("300x150")
    root.configure(background="#c7c7c7")

    key_label = Label(root, text="Activation Key:", background="#c7c7c7", font="Courier 12")
    key_label.pack(pady=10)

    key_entry = Entry(root, font="Courier 12", show="*")
    key_entry.pack()

    activate_button = ttk.Button(root, text="Activate", command=check)
    activate_button.pack(pady=10)
    root.mainloop()

def main():
    root = Tk()
    root.title("Number Systems")
    root.geometry("350x500") 
    root.configure(background="#c7c7c7")

    label_style = ttk.Style()
    label_style.configure(".",        
                    font="Courier 14",   
                    foreground="#404040",  
                    padding=10,            
                    background="#ededed")  

    btn_style = ttk.Style()
    btn_style.configure("TButton", font="Courier 14", foreground="#404040", padding=10, background="#ededed")
    btn_style.map("TButton", background=[("active", "#c7c7c7")])
    btn_style.configure("TButton", relief="flat", focuscolor="#c7c7c7") 

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

    tooltip_label = Label(root, background="#ededed", font="Courier 12", foreground="#404040", height=10, width=35,  wraplength=300)
    tooltip_label.place(y=320)

    root.mainloop()

if __name__ == "__main__":
    save_activation_key("1")
    activation_mode()