import tkinter as tk
class ScreenPet:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=200, height=200)
        self.canvas.pack()
        self.draw_pet()

        # Bind events
        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<Double-Button-1>", self.on_double_click)

    def draw_pet(self):
        self.canvas.delete("all")
        # Draw pet's face
        self.canvas.create_oval(50, 50, 150, 150, fill="yellow", outline="black")
        # Draw eyes
        self.canvas.create_oval(80, 80, 100, 100, fill="black")
        self.canvas.create_oval(120, 80, 140, 100, fill="black")
        # Draw mouth
        self.canvas.create_arc(80, 100, 140, 140, start=0, extent=-180, style=tk.ARC)
    
    def on_left_click(self, event):
        self.draw_pet_happy()
    
    def on_double_click(self, event):
        self.draw_pet_cheeky()

    def draw_pet_happy(self):
        self.draw_pet()
        # Draw blushing cheeks
        self.canvas.create_oval(60, 120, 80, 140, fill="pink", outline="")
        self.canvas.create_oval(140, 120, 160, 140, fill="pink", outline="")

    def draw_pet_cheeky(self):
        self.draw_pet_happy()
        # Draw tongue
        self.canvas.create_polygon(100, 120, 110, 140, 130, 140, 140, 120, fill="red")

root = tk.Tk()
root.title("Screen Pet")
pet = ScreenPet(root)
root.mainloop()
