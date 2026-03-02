import tkinter as tk
from tkinter import messagebox
import json
import sys

# ---------- Load Questions ----------
try:
    with open("questions.json", "r") as file:
        questions = json.load(file)
except FileNotFoundError:
    messagebox.showerror("Error", "questions.json file not found")
    sys.exit()

current_question = 0
score = 0

# ---------- Functions ----------
def load_question():
    question_label.config(text=questions[current_question]["question"])
    selected_option.set(None)

    for i in range(4):
        options[i].config(
            text=questions[current_question]["options"][i],
            value=questions[current_question]["options"][i]
        )

def next_question():
    global current_question, score

    if selected_option.get() is None:
        messagebox.showwarning("Warning", "Please select an answer")
        return

    correct_answer = questions[current_question]["answer"]

    if selected_option.get() == correct_answer:
        score += 1

    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        show_result()

def show_result():
    messagebox.showinfo(
        "Quiz Completed",
        f"Your Score: {score} / {len(questions)}"
    )
    root.destroy()

# ---------- GUI ----------
root = tk.Tk()
root.title("Tkinter Quiz App")
root.geometry("500x350")
root.resizable(False, False)

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    wraplength=450
)
question_label.pack(pady=20)

selected_option = tk.StringVar()

options = []
for _ in range(4):
    rb = tk.Radiobutton(
        root,
        text="",
        variable=selected_option,
        value="",
        font=("Arial", 11)
    )
    rb.pack(anchor="w", padx=50)
    options.append(rb)

tk.Button(
    root,
    text="Next",
    width=15,
    command=next_question
).pack(pady=25)

load_question()
root.mainloop()