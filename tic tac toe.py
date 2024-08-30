import tkinter as tk
from tkinter import messagebox

def check_winner():
    #all possible winning combinations
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        #if all three buttons in a combo have the same non-empty text, we have a winner
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            #highlight the winning buttons
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            #announce winner in messagebox
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!")
            #exit game
            root.quit()

def button_click(index):
    global winner
    #if the button is not already clicked and no winner has been declared
    if buttons[index]["text"] == "" and not winner:
        #set the button's text to the current player's symbol (X or O)
        buttons[index]["text"] = current_player
        #check if this move wins the game
        check_winner()
        #switch to the other player
        toggle_player()

def toggle_player():
    global current_player
    #toggle between players X and O
    current_player = "X" if current_player == "O" else "O"
    #update the label to show whose turn it is
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic Tac Toe")

#heading
heading = tk.Label(root, text="Tic Tac Toe", font=("Arial", 30, "bold"), fg="blue")
heading.grid(row=0, column=0, columnspan=3, pady=(10, 5))

#subheading
subheading = tk.Label(root, text="Player vs Player", font=("Arial", 20), fg="gray")
subheading.grid(row=1, column=0, columnspan=3, pady=(0, 20))

#3x3 grid buttons
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

#arrange buttons in grid
for i, button in enumerate(buttons):
    button.grid(row=(i // 3) + 2, column=i % 3)

#initialize the game
#X starts
current_player = "X"
#No winner
winner = False

#turn label
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=5, column=0, columnspan=3, pady=10)

#start the tkinter loop
root.mainloop()