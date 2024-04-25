import tkinter as tk
import random

WIDTH = 500
HEIGHT = 500
DELAY = 150
UNIT_SIZE = 20

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(100,100),(80,100),(60,100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0

        self.bind_keys()
        self.move_snake()

    def bind_keys(self):
        self.master.bind("<Up>", lambda event: self.change_direction("Up"))
        self.master.bind("<Down>", lambda event: self.change_direction("Down"))
        self.master.bind("<Left>", lambda event: self.change_direction("Left"))
        self.master.bind("<Right>", lambda event: self.change_direction("Right"))

    def create_food(self):
        x = random.randint(0, (WIDTH - UNIT_SIZE) // UNIT_SIZE) * UNIT_SIZE
        y = random.randint(0, (HEIGHT - UNIT_SIZE) // UNIT_SIZE) * UNIT_SIZE
        return x,y 
    
    def move_snake(self):
        head = self.snake[0]
        new_head = ()

        if self.direction == "Up":
            new_head = (head[0], head[1] - UNIT_SIZE)
        elif self.direction == "Down":
            new_head = (head[0], head[1]+UNIT_SIZE)
        elif self.direction == "Left":
            new_head = (head[0]-UNIT_SIZE, head[1])
        elif self.direction == "Right":
            new_head = (head[0]+UNIT_SIZE, head[1])

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.scope += 1
            self.food = self.create_food()
        else:
            self.snake.pop()

        
        self.draw()
        self.check_collision()
        self.master.after(DELAY, self.move_snake)

    def draw(self):
        self.canvas.delete("all")
        self.canvas.create_text(50,10,text=f"Score: {self.score}", fill="white")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0]+UNIT_SIZE, self.food[1]+UNIT_SIZE, fill="red")

        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + UNIT_SIZE, segment[1]+UNIT_SIZE, fill="green")

    def change_direction(self, direction):
        if direction == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif direction == "Down" and self.direction != "Up":
            self.direction = "Left"
        elif direction == "Right" and self.direction != "Right":
            self.direction = "Right"

    def check_collision(self):
        head = self.snake[0]
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            self.game_over()
            return 
        
        if head in self.snake[1:]:
            self.game_over()
            return 
        
    def game_over(self):
        self.game_over()
        return 
    
    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text=f"Game Over! Your score: {self.score}", fill="white")

def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
