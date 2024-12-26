import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class CircleQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Circle Properties Quiz")

        # Load images and questions
        self.questions = [
            {"image_path": r"Circles\ (1).png", "property": "∠ in semi-circle"},
            {"image_path": r"Circles\ (2).png", "property": "∠ at centre twice ∠ at circumference"},
            {"image_path": r"Circles\ (3).png", "property": "chords equidistant from centre eq."},
            {"image_path": r"Circles\ (4).png", "property": "eq. chords equidistant from centre"},
            {"image_path": r"Circles\ (5).png", "property": "⊥bisector of chord passes through centre"},
            {"image_path": r"Circles\ (6).png", "property": "line joining centre and mid-pt. of chord ⊥chord"},
            {"image_path": r"Circles\ (7).png", "property": "⊥from centre to chord bisects chord"},
            {"image_path": r"Circles\ (8).png", "property": "∠ in alt. segment"},
            {"image_path": r"Circles\ (9).png", "property": "tangent properties"},
            {"image_path": r"Circles\ (10).png", "property": "ext.∠ = int. opp.∠"},
            {"image_path": r"Circles\ (11).png", "property": "opp.∠s supp"},
            {"image_path": r"Circles\ (12).png", "property": "converse of ∠s in the same segment"},
            {"image_path": r"Circles\ (13).png", "property": "ext.∠s, cyclic quad."},
            {"image_path": r"Circles\ (14).png", "property": "opp.∠s, cyclic quad."},
            {"image_path": r"Circles\ (15).png", "property": "ext.∠ of ∆"},
            {"image_path": r"Circles\ (16).png", "property": "∠sum of∆"},
            {"image_path": r"Circles\ (17).png", "property": "int.∠s, AB//PQ"},
            {"image_path": r"Circles\ (18).png", "property": "alt. ∠s, AB//PQ"},
            {"image_path": r"Circles\ (19).png", "property": "corr. ∠s AB//PQ"},
            {"image_path": r"Circles\ (20).png", "property": "vert. opp. ∠s"},
            {"image_path": r"Circles\ (21).png", "property": "∠s at a pt."},
            {"image_path": r"Circles\ (22).png", "property": "adj. ∠s on the st. line"},
            {"image_path": r"Circles\ (23).png", "property": "∠s in the same segment"},
            {"image_path": r"Circles\ (24).png", "property": "equal arcs, equal ∠s"},
            {"image_path": r"Circles\ (25).png", "property": "equal chords, equal ∠s"},
            {"image_path": r"Circles\ (26).png", "property": "equal arcs, equal chords"},
            {"image_path": r"Circles\ (27).png", "property": "arcs prop. to ∠s at centre"},
            {"image_path": r"Circles\ (28).png", "property": "arcs prop. to ∠s at circumference"},
        ]

        random.shuffle(self.questions)
        self.current_question_index = 0

        # UI Elements
        self.canvas = tk.Canvas(root, width=500, height=400)
        self.canvas.pack()

        self.question_label = tk.Label(root, text="What is the property of the shown circle diagram?", wraplength=400, font=("Arial", 12))
        self.question_label.pack(pady=10)

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(root, textvariable=self.answer_var, font=("Arial", 12), width=30)
        self.answer_entry.pack(pady=5)

        self.symbol_buttons_frame = tk.Frame(root)
        self.symbol_buttons_frame.pack()

        symbols = ["∠","∆","⊥", "//"]
        for symbol in symbols:
            btn = tk.Button(self.symbol_buttons_frame, text=symbol, command=lambda s=symbol: self.insert_symbol(s), font=("Arial", 12))
            btn.pack(side=tk.LEFT, padx=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
        self.feedback_label.pack(pady=10)

        self.progress_label = tk.Label(root, text="", font=("Arial", 10))
        self.progress_label.pack(pady=10)

        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            try:
                image = Image.open(question["image_path"])
                image = image.resize((400, 400))
                self.photo = ImageTk.PhotoImage(image)
                self.canvas.create_image(50, 50, anchor=tk.NW, image=self.photo)
            except Exception as e:
                self.canvas.delete("all")
                self.canvas.create_text(250, 200, text="Image not found", font=("Arial", 16), fill="red")

            self.answer_var.set("")
            self.feedback_label.config(text="")
            self.update_progress()
        else:
            if messagebox.askyesno("Quiz Completed", "You have completed the quiz! Do you want to restart?"):
                random.shuffle(self.questions)
                self.current_question_index = 0
                self.display_question()
            else:
                self.root.quit()

    def check_answer(self):
        correct_answer = self.questions[self.current_question_index]["property"]
        self.feedback_label.config(text=f"Correct Answer: {correct_answer}", fg="blue")

    def next_question(self):
        self.current_question_index += 1
        self.display_question()

    def insert_symbol(self, symbol):
        cursor_pos = self.answer_entry.index(tk.INSERT)
        current_text = self.answer_var.get()
        new_text = current_text[:cursor_pos] + symbol + current_text[cursor_pos:]
        self.answer_var.set(new_text)
        self.answer_entry.icursor(cursor_pos + len(symbol))

    def update_progress(self):
        self.progress_label.config(text=f"Question {self.current_question_index + 1} of {len(self.questions)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CircleQuizApp(root)
    root.mainloop()
