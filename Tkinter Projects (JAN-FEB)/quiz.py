import tkinter as tk

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz")
        self.root.configure(bg="#1F2833")

        self.questions = [
            "What is 15+20",
            "Who wrote Romeo and Juliet?",
            "How much is 23+32",
            "Which is State of Maharashtra?",
        ]

        self.answers = [
            "35",
            "William Shakespeare",
            "55",
            "Mumbai"
        ]

        self.current_ques = 0
        self.score = 0

        self.label = tk.Label(root, text=self.questions[self.current_ques])
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.submit_button = tk.Button(root, text='Submit',command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
        user_ans = self.entry.get()
        correct_ans = self.answers[self.current_ques]

        if user_ans.lower() == correct_ans.lower():
            self.score += 1

        self.current_ques +=1

        if self.current_ques<len(self.questions):
            self.label.config(text=self.questions[self.current_ques])
            self.entry.delete(0, tk.END)
        else:
            self.label.config(text=f"Quiz Complete! Your Score is : {self.score}/{len(self.questions)}")
            self.entry.pack_forget()
            self.submit_button.pack_forget()

root = tk.Tk()
root.geometry("200x100")
quiz = Quiz(root)
root.mainloop()

