import tkinter as tk
import datetime

from app.session import load_session
from modules.scheduler import schedule_mail
from modules.notifier import reminder_popup

email, _ = load_session()


def open_mail_window():
    if not email:
        tk.messagebox.showerror("Login Required", "Please login first")
        return

    win = tk.Toplevel()
    win.title("Daily Work Mail")
    win.geometry("900x550")
    win.configure(bg="#f1f3f4")

    
    sidebar = tk.Frame(win, bg="#e8eaed", width=200)
    sidebar.pack(side="left", fill="y")

    tk.Label(
        sidebar,
        text="📧 Mail",
        font=("Helvetica", 16, "bold"),
        bg="#e8eaed"
    ).pack(pady=20)

    for item in ["Inbox", "Sent", "Drafts", "HR Reports"]:
        tk.Label(
            sidebar,
            text=item,
            bg="#e8eaed",
            font=("Helvetica", 12),
            anchor="w",
            padx=20
        ).pack(fill="x", pady=6)

    # ---------------- Main Area ----------------
    main = tk.Frame(win, bg="white")
    main.pack(side="right", fill="both", expand=True)

    tk.Label(
        main,
        text="New Message",
        font=("Helvetica", 18, "bold"),
        bg="white"
    ).pack(anchor="w", padx=20, pady=15)

    form = tk.Frame(main, bg="white")
    form.pack(fill="both", expand=True, padx=20)

    # ----------- FROM -----------
    tk.Label(form, text="From", bg="white").grid(row=0, column=0, sticky="w")
    from_entry = tk.Entry(form, width=80)
    from_entry.insert(0, email)
    from_entry.config(state="readonly")
    from_entry.grid(row=0, column=1, pady=5, sticky="w")

    # ----------- TO -----------
    tk.Label(form, text="To", bg="white").grid(row=1, column=0, sticky="w")
    to_entry = tk.Entry(form, width=80)
    to_entry.insert(0, "hr@company.com")
    to_entry.grid(row=1, column=1, pady=5, sticky="w")

    # ----------- DATE -----------
    tk.Label(form, text="Date", bg="white").grid(row=2, column=0, sticky="w")
    date_entry = tk.Entry(form, width=30)
    date_entry.insert(0, datetime.date.today().strftime("%d %b %Y"))
    date_entry.config(state="readonly")
    date_entry.grid(row=2, column=1, sticky="w", pady=5)

    # ----------- CURRENT TIME -----------
    tk.Label(form, text="Current Time", bg="white").grid(row=3, column=0, sticky="w")
    time_now_entry = tk.Entry(form, width=30)
    time_now_entry.grid(row=3, column=1, sticky="w", pady=5)
    time_now_entry.config(state="readonly")

    # ----------- SUBJECT -----------
    tk.Label(form, text="Subject", bg="white").grid(row=4, column=0, sticky="w")
    subject_entry = tk.Entry(form, width=80)
    subject_entry.grid(row=4, column=1, pady=5, sticky="w")

    # ----------- BODY -----------
    body = tk.Text(form, height=12, font=("Helvetica", 11))
    body.grid(row=5, column=0, columnspan=2, pady=15, sticky="w")

    # ----------- SEND TIME -----------
    tk.Label(form, text="Send Time (HH:MM)", bg="white").grid(row=6, column=0, sticky="w")
    time_entry = tk.Entry(form, width=20)
    time_entry.grid(row=6, column=1, sticky="w")

    # ----------- STATUS BAR -----------
    status = tk.Label(main, text="", fg="green", bg="white")
    status.pack(side="left", padx=20)

    # ----------- LIVE CLOCK -----------
    def update_time():
        now = datetime.datetime.now().strftime("%H:%M:%S")
        time_now_entry.config(state="normal")
        time_now_entry.delete(0, tk.END)
        time_now_entry.insert(0, now)
        time_now_entry.config(state="readonly")
        win.after(1000, update_time)

    update_time()

    # ----------- SCHEDULE MAIL -----------
    def schedule():
        if not time_entry.get() or not subject_entry.get():
            status.config(text="❌ Subject and time required", fg="red")
            return

        schedule_mail(
            time_entry.get(),
            subject_entry.get(),
            body.get("1.0", tk.END),
            to_entry.get()
        )

        reminder_popup(time_entry.get())

        status.config(
            text=f"📅 Mail scheduled for {date_entry.get()} at {time_entry.get()}",
            fg="green"
        )

    tk.Button(
        main,
        text="📤 Schedule & Send",
        bg="#1a73e8",
        fg="white",
        command=schedule
    ).pack(side="right", padx=20, pady=15)
