import random
import string
import tkinter as tk
from tkinter import Label, Entry, Button, Checkbutton, IntVar

import pyperclip

generated_passwords = set()


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_chars = random.choice(characters)
        pwd += new_chars

        if new_chars in digits:
            has_number = True
        elif new_chars in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special

    return pwd


def generate_and_display_password():
    min_length = int(min_length_entry.get())
    has_number = has_number_var.get() == 1
    has_special = has_special_var.get() == 1

    while True:
        pwd = generate_password(min_length, has_number, has_special)
        if pwd not in generated_passwords:
            generated_passwords.add(pwd)
            break

    result_label.config(text="Generated Password: " + pwd)
    pyperclip.copy(pwd)  # Copy password to clipboard


def copy_password_to_clipboard():
    if result_label.cget("text") != "":
        pyperclip.copy(result_label.cget("text")[19:])  # Extracting the password from the label text


# Create the main window
root = tk.Tk()
root.title("Python Password Generator")

# Create main label
main_label = Label(root, text="Python Password Generator", font=("Helvetica", 30))
main_label.pack(pady=10)

# Create and pack widgets
Label(root, text="Enter the minimum length:").pack()
min_length_entry = Entry(root)
min_length_entry.pack()

has_number_var = IntVar()
Checkbutton(root, text="Include numbers", variable=has_number_var).pack()

has_special_var = IntVar()
Checkbutton(root, text="Include special characters", variable=has_special_var).pack()

generate_button = Button(
    root,
    text="Generate Password",
    command=generate_and_display_password,
    bg='#45b592',
    fg='#ffffff',
    bd=0
)
generate_button.pack()

copy_button = Button(
    root,
    text="Copy Password",
    command=copy_password_to_clipboard,
    bg='#45b592',
    fg='#ffffff',
    bd=0
)
copy_button.pack()

result_label = Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
