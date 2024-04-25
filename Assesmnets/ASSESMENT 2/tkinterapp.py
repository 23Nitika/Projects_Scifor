import tkinter as tk 
from tkinter import messagebox

class PersonalizedGreetingsApp:
    def __init__(self, master):
        self.master = master
        master.title("Personalized Greeting App")

        self.label = tk.Label(master, text="Enter your name:")
        self.label.pack()

        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.greet_button = tk.Button(master, text="Greet", command=self.display_greeting)
        self.greet_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command = master.quit)
        self.quit_button.pack()

    def display_greeting(self):
        name = self.name_entry.get()
        if name:
            greeting_message = f"Hello, {name}! Welcome to Personalized Greeting App."
            self.show_message("Greetings", greeting_message)
        else:
            self.show_message("Error", "Please enter your name.")
    
    def show_message(self, title, message):
        messagebox.showinfo(title, message)


root = tk.Tk()
root.geometry("300x200")
app = PersonalizedGreetingsApp(root)
root.mainloop()