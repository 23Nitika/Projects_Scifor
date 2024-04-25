import tkinter as tk
from tkinter import colorchooser, messagebox

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App Replica")
        self.root.geometry("800x600")
        
        self.pen_color = "black"
        self.brush_size = 5
        self.tool = "pen"

        self.create_widgets()
    
    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, bg="white", bd =2, relief=tk.SUNKEN)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.pen_button = tk.Button(self.root, text="Pen", command=lambda: self.set_tool("pen"))
        self.pen_button.pack(side=tk.LEFT)

        self.brush_button = tk.Button(self.root, text="Brush", command=lambda: self.set_tool("brush"))
        self.brush_button.pack(side=tk.LEFT)

        self.color_button = tk.Button(self.root, text="Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT)

        self.eraser_button = tk.Button(self.root, text="Eraser", command=lambda: self.set_tool("eraser"))
        self.eraser_button.pack(side=tk.LEFT)

        self.size_scale = tk.Scale(self.root, from_=1, to=20, orient=tk.HORIZONTAL, command=self.set_size)
        self.size_scale.set(5)
        self.size_scale.pack(side=tk.LEFT)

        self.canvas.bind("<B1-Motion>", self.draw)

    def set_tool(self, tool):
        self.tool = tool

    def choose_color(self):
        self.pen_color = colorchooser.askcolor()[1]
    
    def set_size(self, size):
        self.brush_size = int(size)

    def draw(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        if self.tool == "pen":
            self.canvas.create_line(x1, y1, x2, y2, fill=self.pen_color, width=self.brush_size * 2)
        elif self.tool == "brush":
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.pen_color, outline="")
        elif self.tool == "eraser":
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()