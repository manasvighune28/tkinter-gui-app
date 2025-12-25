import tkinter as tk
from app.db import get_connection

def open_form_window():
    win = tk.Toplevel()
    win.title("Data Entry Form")
    win.geometry("420x350")
    win.configure(bg="#a1aaac")

    # ---------- Header ----------
    title = tk.Label(
        win,
        text="📝 Data Entry Form",
        font=("Helvetica", 16, "bold"),
        bg="#ecf0f1",
        fg="#2c3e50"
    )
    title.pack(pady=15)

    # ---------- Card ----------
    card = tk.Frame(
        win,
        bg="white",
        bd=0
    )
    card.pack(padx=30, pady=10, fill="both", expand=True)

    # ---------- Name ----------
    tk.Label(
        card,
        text="Name",
        font=("Helvetica", 11),
        bg="white",
        fg="#e3d96a"
    ).pack(pady=(20, 5))

    name = tk.Entry(
        card,
        font=("Helvetica", 12),
        justify="center"
    )
    name.pack(pady=5)

    # ---------- Email ----------
    tk.Label(
        card,
        text="Email",
        font=("Helvetica", 11),
        bg="white",
        fg="#1382f0"
    ).pack(pady=(15, 5))

    email = tk.Entry(
        card,
        font=("Helvetica", 12),
        justify="center"
    )
    email.pack(pady=5)

    # ---------- Status ----------
    status = tk.Label(
        card,
        text="",
        font=("Helvetica", 11, "bold"),
        bg="white",
        fg="#27ae60"
    )
    status.pack(pady=15)

    # ---------- Save Function ----------
    def save_data():
        if not name.get().strip() or not email.get().strip():
            status.config(text="⚠️ All fields are required", fg="#e67e22")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO entries (name, email) VALUES (%s, %s)",
                (name.get(), email.get())
            )
            conn.commit()

            cursor.close()
            conn.close()

            status.config(text="✅ Saved successfully", fg="#27ae60")
            name.delete(0, tk.END)
            email.delete(0, tk.END)

        except Exception:
            status.config(text="❌ Database error", fg="#c0392b")

    # ---------- Button ----------
    tk.Button(
        card,
        text="Save",
        font=("Helvetica", 12),
        bg="#2ecc71",
        fg="white",
        activebackground="#27ae60",
        activeforeground="white",
        relief="flat",
        padx=25,
        pady=8,
        command=save_data
    ).pack(pady=10)
