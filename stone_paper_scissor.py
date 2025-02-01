import random
import tkinter as tk
from tkinter import messagebox

def game(user_choice):
    computer_choice = random.choice(["stone", "paper", "scissor"])
    result = ""

    if user_choice == computer_choice:
        result = "It's a draw!"
    elif (user_choice == "stone" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        result = "YOU ARE THE WINNER!"
    else:
        result = "COMPUTER IS THE WINNER!"

    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer choice: {computer_choice}\n{result}")

root = tk.Tk()
root.title("stone Paper Scissors")

button_stone = tk.Button(root, text="Stone", command=lambda: game("stone"))
button_paper = tk.Button(root, text="Paper", command=lambda: game("paper"))
button_scissor = tk.Button(root, text="Scissor", command=lambda: game("scissor"))

button_stone.pack(pady=40)
button_paper.pack(pady=40)
button_scissor.pack(pady=40)
root.mainloop()



