# Password Generator ApplicationS
import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


def generate_password(length, use_upper, use_lower, use_digits, use_specials):
    if not any([use_upper, use_lower, use_digits, use_specials]):
        return "Please select at least one character type."

    char_pools = []
    mandatory_chars = []

    if use_upper:
        char_pools.append(string.ascii_uppercase)
        mandatory_chars.append(random.choice(string.ascii_uppercase))
    if use_lower:
        char_pools.append(string.ascii_lowercase)
        mandatory_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        char_pools.append(string.digits)
        mandatory_chars.append(random.choice(string.digits))
    if use_specials:
        char_pools.append("!@#$%^&*()-_=+[]{};:,.<>?")

        mandatory_chars.append(random.choice("!@#$%^&*()-_=+[]{};:,.<>?"))

    all_chars = ''.join(char_pools)
    if length < len(mandatory_chars):
        return "Length too short for selected options."

    remaining_length = length - len(mandatory_chars)
    password = mandatory_chars + random.choices(all_chars, k=remaining_length)
    random.shuffle(password)

    return ''.join(password)


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Generator")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        tk.Label(root, text="Password Length:").pack(pady=5)
        self.length_var = tk.IntVar(value=12)
        tk.Spinbox(root, from_=4, to=64, textvariable=self.length_var, width=5).pack()

        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_specials = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.use_upper).pack(anchor='w', padx=20)
        tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.use_lower).pack(anchor='w', padx=20)
        tk.Checkbutton(root, text="Include Numbers", variable=self.use_digits).pack(anchor='w', padx=20)
        tk.Checkbutton(root, text="Include Special Characters", variable=self.use_specials).pack(anchor='w', padx=20)

        tk.Button(root, text="Generate Password", command=self.on_generate).pack(pady=10)

        self.result_entry = tk.Entry(root, font=("Courier", 12), justify='center')
        self.result_entry.pack(fill='x', padx=20, pady=5)

        tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)

    def on_generate(self):
        length = self.length_var.get()
        result = generate_password(
            length,
            self.use_upper.get(),
            self.use_lower.get(),
            self.use_digits.get(),
            self.use_specials.get()
        )
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, result)

    def copy_to_clipboard(self):
        password = self.result_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")


if __name__ == "__main__":
    try:
        import pyperclip
    except ImportError:
        import subprocess
        subprocess.check_call(["pip", "install", "pyperclip"])
        import pyperclip

    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
# This code is a simple password generator application using Tkinter for the GUI.
# It allows users to specify the length and character types for the password.