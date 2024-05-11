import tkinter as tk
from gui import get_user_info, center_window
from data_handler import save_data

def vote():
    """ Handle the voting process. """
    root = tk.Tk()
    root.withdraw()
    user_info = get_user_info(root)
    if user_info:
        name, location, dob = user_info
        root.deiconify()
        root.title("Vote for Candidate")
        center_window(root, 400, 200)
        tk.Label(root, text="Choose a candidate:").pack(pady=20)

        # Buttons for candidates
        for candidate in ["John", "Jane"]:
            tk.Button(root, text=candidate, command=lambda c=candidate: [save_data({'Name': name, 'Location': location, 'DOB': dob}, c), root.destroy()]).pack(pady=10)

        root.mainloop()
    else:
        root.destroy()

if __name__ == "__main__":
    vote()
