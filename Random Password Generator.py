import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showwarning("Input Error", "Password length should be at least 4.")
            return
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number for length.")
        return
    
    # Define character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "Generate a password first to copy.")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")

# Label and entry for password length
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_length = tk.Entry(root, width=10)
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Entry for generated password
tk.Label(root, text="Generated Password:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_password = tk.Entry(root, width=30)
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Generate and Copy buttons
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, padx=10, pady=20)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=2, column=1, padx=10, pady=20)

# Run the application
root.mainloop()
