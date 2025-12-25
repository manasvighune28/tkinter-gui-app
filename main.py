import tkinter as tk

from modules.news import open_news_window
from modules.weather import open_weather_window
from modules.form import open_form_window
from modules.mail import open_mail_window

from app.session import load_session
from app.auth import open_login


def build_dashboard(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(
        root,
        text="📊 Tkinter GUI Projects",
        font=("Helvetica", 16, "bold")
    ).pack(pady=20)

    tk.Button(root, text="📰 News Headlines", width=25,
              command=open_news_window).pack(pady=8)

    tk.Button(root, text="🌦 Weather App", width=25,
              command=open_weather_window).pack(pady=8)

    tk.Button(root, text="📝 Data Entry Form", width=25,
              command=open_form_window).pack(pady=8)

    tk.Button(
        root,
        text="📧 Daily Work Mail",
        width=25,
        bg="#1a73e8",
        fg="white",
        font=("Helvetica", 11, "bold"),
        command=open_mail_window
    ).pack(pady=12)


def main():
    root = tk.Tk()
    root.title("Tkinter GUI Projects")
    root.geometry("450x420")

    email, _ = load_session()

    if email:
        build_dashboard(root)
    else:
        open_login(root, lambda: build_dashboard(root))

    root.mainloop()


if __name__ == "__main__":
    main()
