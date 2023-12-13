import tkinter as tk
from tkinter import ttk
import pyperclip


conversions = {
    1: "Uppercase",
    2: "Lowercase",
    3: "Capitalize",
    4: "Title",
    5: "SwapCase",
}

class CaseConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Case Converter")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Enter the sentence here:").pack(pady=10)
        self.user_entry = ttk.Entry(self.root, width=40)
        self.user_entry.pack(pady=10)

        ttk.Label(self.root, text="Choose an option to continue:").pack(pady=5)
        self.choice_var = tk.StringVar()
        self.choice_combobox = ttk.Combobox(
            self.root, values=list(conversions.values()), state="readonly"
        )
        self.choice_combobox.pack(pady=10)

        ttk.Button(self.root, text="Convert", command=self.perform_conversion).pack(
            pady=10
        )

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        ttk.Button(self.root, text="Click here to copy", command=self.copy_to_clipboard).pack(pady=10)

    def perform_conversion(self):
        uservalue = self.user_entry.get()

        if uservalue.isnumeric():
            self.result_label["text"] = "Only string characters allowed!"
            return

        choice = list(conversions.keys())[list(conversions.values()).index(self.choice_combobox.get())]
        operation = conversions[choice]
        newvalue = apply_conversion(uservalue, operation)

        self.result_label["text"] = f"Your Output ({operation}): {newvalue}"

    def copy_to_clipboard(self):
        result_text = self.result_label.cget("text")
        if result_text:
            pyperclip.copy(result_text)

def apply_conversion(value, operation):
    if operation == "Uppercase":
        return value.upper()
    elif operation == "Lowercase":
        return value.lower()
    elif operation == "Capitalize":
        return value.capitalize()
    elif operation == "Title":
        return value.title()
    elif operation == "SwapCase":
        return value.swapcase()

if __name__ == "__main__":
    root = tk.Tk()
    app = CaseConverterApp(root)
    root.mainloop()
