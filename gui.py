import tkinter as tk
from tkinter import messagebox
from data_handler import save_data, validate_date

def center_window(window, width, height):
    """ Centers the window on the screen. """
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x}+{y}")

def custom_input_dialog(title, prompt, parent, validate_func=None, width=300, height=200):
    """ Custom input dialog that allows size control, centers it, and validates input. """
    while True:
        dialog = tk.Toplevel(parent)
        dialog.title(title)
        center_window(dialog, width, height)
        tk.Label(dialog, text=prompt).pack(pady=10)
        input_var = tk.StringVar(dialog)
        entry = tk.Entry(dialog, textvariable=input_var)
        entry.pack(pady=10)
        entry.focus_set()

        def on_submit():
            if validate_func and not validate_func(input_var.get()):
                messagebox.showerror("Invalid Input", "Please enter a valid input.")
                entry.delete(0, tk.END)  # Clears the input field for new input
            else:
                dialog.destroy()

        tk.Button(dialog, text="Submit", command=on_submit).pack(pady=10)
        parent.wait_window(dialog)  # Waits for the dialog to close
        if input_var.get() and (not validate_func or validate_func(input_var.get())):
            return input_var.get()

def get_user_info(root):
    """ Prompts for user's name, location, and date of births. """
    name = custom_input_dialog("Name", "Enter your name:", root)
    location = custom_input_dialog("Location", "Enter your location:", root)
    dob = custom_input_dialog("Date of Birth", "Enter your date of birth (YYYY-MM-DD):", root, validate_func=validate_date)
    if all([name, location, dob]):
        return name, location, dob
    return None
