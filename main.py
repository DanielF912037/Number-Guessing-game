import random
import math
import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Function to start and control the game
def play_game():
    # Get the selected game mode (integer or decimal)
    game_mode = game_mode_var.get()

    try:
        # Get lower and upper bounds from user input
        lower = float(lower_entry.get())
        upper = float(upper_entry.get())
    except ValueError:
        # Show an error message if input is not a valid number
        messagebox.showerror("Error", "Invalid input for lower or upper bound.")
        return

    if game_mode == "integer":
        # Generate a random integer within the specified bounds
        x = random.randint(int(lower), int(upper))
    else:
        # Generate a random decimal within the specified bounds
        x = random.uniform(lower, upper)

    # Calculate the number of chances based on the range
    chances = round(math.log(upper - lower + 1, 2))
    chances_label.config(text=f"You have {chances} chances to guess the number.")

    count = 0

    # Function to handle user's guess
    def make_guess():
        nonlocal count
        count += 1
        guess = float(guess_entry.get())

        if x == guess:
            # Display a congratulatory message if the guess is correct
            messagebox.showinfo("Congratulations", f"You guessed it in {count} tries!")
            reset_game()
        elif x > guess:
            result_label.config(text="You guessed too small!")
        elif x < guess:
            result_label.config(text="You guessed too high!")


        # Calculate and display the remaining guesses
        remaining_guesses = chances - count
        if remaining_guesses > 0:
            chances_label.config(text=f"You have {remaining_guesses} guesses left.")
        else:
            chances_label.config(text="No more guesses left.")


        if count >= chances:
            # If the user exhausts all chances, show the correct answer and reset the game
            messagebox.showinfo("Game Over", f"The number was {x}. Better luck next time!")
            reset_game()

    # Function to reset the game
    def reset_game():
        nonlocal count
        count = 0
        guess_entry.delete(0, "end")
        result_label.config(text="")
        guess_button.config(state="normal")
        reset_button.config(state="normal")

    # Configure buttons to use the corresponding functions
    guess_button.config(command=make_guess, state="normal")
    reset_button.config(command=reset_game, state="normal")

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")

# Customize the font for labels
custom_font = font.Font(family="Arial", size=14, weight="bold")

# Create a variable to hold the game mode choice
game_mode_var = tk.StringVar(value="integer")

# Create labels for game mode selection
game_mode_label = tk.Label(root, text="Choose the game mode:", font=custom_font)
game_mode_label.pack()

# Create a frame to hold radio buttons for game mode selection
game_mode_frame = tk.Frame(root)
game_mode_frame.pack()

# Create radio buttons for selecting the game mode
game_mode_radio_integer = tk.Radiobutton(game_mode_frame, text="Integer", variable=game_mode_var, value="integer")
game_mode_radio_integer.pack(side="left")
game_mode_radio_decimal = tk.Radiobutton(game_mode_frame, text="Decimal", variable=game_mode_var, value="decimal")
game_mode_radio_decimal.pack(side="left")

# Create input fields for lower and upper bounds
lower_label = tk.Label(root, text="Enter Lower bound:")
lower_label.pack()
lower_entry = tk.Entry(root)
lower_entry.pack()

upper_label = tk.Label(root, text="Enter Upper bound:")
upper_label.pack()
upper_entry = tk.Entry(root)
upper_entry.pack()

# Button to start the game
start_button = tk.Button(root, text="Start Game", command=play_game)
start_button.pack()

# Label to display the remaining chances
chances_label = tk.Label(root, text="")
chances_label.pack()

# Label and entry field for user guesses
guess_label = tk.Label(root, text="Enter your guess:")
guess_label.pack()
guess_entry = tk.Entry(root)
guess_entry.pack()

# Button to make a guess
guess_button = tk.Button(root, text="Guess", state="disabled")
guess_button.pack()

# Label to display the result of the guess
result_label = tk.Label(root, text="")
result_label.pack()

# Button to reset the game
reset_button = tk.Button(root, text="Reset Game", state="disabled")
reset_button.pack()

# Start the GUI main loop
root.mainloop()