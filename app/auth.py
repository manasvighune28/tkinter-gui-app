import tkinter as tk
from app.session import save_session

def open_login(root, on_success):
    win = tk.Toplevel(root)
    win.title("Employee Login")
    win.geometry("400x300")
    win.transient(root)
    win.grab_set()

    tk.Label(win, text="Gmail Login", font=("Helvetica", 16, "bold")).pack(pady=20)

    tk.Label(win, text="Gmail Address").pack()
    email_entry = tk.Entry(win, width=40)
    email_entry.pack(pady=5)

    tk.Label(win, text="Gmail App Password").pack()
    pass_entry = tk.Entry(win, show="*", width=40)
    pass_entry.pack(pady=5)

    status = tk.Label(win, text="", fg="red")
    status.pack(pady=10)

    def login():
        email = email_entry.get()
        password = pass_entry.get()

        if not email or not password:
            status.config(text="All fields required")
            return

        save_session(email, password)
        win.destroy()
        on_success()

    tk.Button(win, text="Login", command=login).pack(pady=15)
