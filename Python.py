import tkinter as tk

class QuestionApp:
    def __init__(self, root):
        self.root = root
        self.question_index = 0

        self.questions = [
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "Which planet is closest to the sun?", "answer": "Mercury"},
            # Add more questions here...
        ]

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="")
        self.question_label.pack()

        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.feedback_label = tk.Label(self.root, text="")
        self.feedback_label.pack()

        self.display_question()

    def display_question(self):
        if self.question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.question_index]["question"])
        else:
            self.question_label.config(text="Quiz completed!")

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.questions[self.question_index]["answer"].lower()

        if user_answer == correct_answer:
            self.feedback_label.config(text="Correct!")
        else:
            self.feedback_label.config(text="Incorrect!")

        self.question_index += 1
        self.display_question()


root = tk.Tk()
app = QuestionApp(root)
root.mainloop()
