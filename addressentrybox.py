import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    address = entry_address.get()
    city = entry_city.get()
    state = entry_state.get()
    zip_code = entry_zip.get()

    if not name or not address or not city or not state or not zip_code:
        messagebox.showwarning("Input Error", "All fields must be filled out.")
    else:
        # Display or store the entered data
        messagebox.showinfo("Form Submitted", f"Name: {name}\nAddress: {address}\nCity: {city}\nState: {state}\nZIP: {zip_code}")
        clear_form()

# Function to clear form fields
def clear_form():
    entry_name.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_state.delete(0, tk.END)
    entry_zip.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Address Entry Form")
root.geometry("400x300")

# Labels and entry fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Address:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_address = tk.Entry(root, width=30)
entry_address.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="City:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
entry_city = tk.Entry(root, width=30)
entry_city.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="State:").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
entry_state = tk.Entry(root, width=30)
entry_state.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="ZIP Code:").grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
entry_zip = tk.Entry(root, width=30)
entry_zip.grid(row=4, column=1, padx=10, pady=10)

# Submit and Clear buttons
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, column=0, padx=10, pady=20)

clear_button = tk.Button(root, text="Clear", command=clear_form)
clear_button.grid(row=5, column=1, padx=10, pady=20)

# Run the application
root.mainloop()
