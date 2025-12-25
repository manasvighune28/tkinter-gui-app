📧 Tkinter GUI Mail Scheduler Application

A desktop-based Tkinter GUI application built with Python that integrates News, Weather, Data Entry, and a Gmail-like Mail Scheduler.
Employees can log in once using their Gmail App Password and schedule daily work emails to HR with reminder notifications.

🚀 Features
📰 News Headlines

Fetches latest news using free public APIs

Clean GUI display

🌦 Weather Application

Real-time weather data by city

Uses free Weather API

📝 Data Entry Form

Stores employee data in MySQL

Simple and secure CRUD operation

📧 Daily Work Mail (Core Feature)

Gmail-like mail UI

Login once using Gmail App Password

Encrypted session storage (Fernet)

Schedule mail delivery (HH:MM)

Background scheduler thread

SMTP-based real email delivery

Reminder popup notification

🛠 Tech Stack

Python 3.10

Tkinter (GUI)

smtplib (Gmail SMTP)

cryptography (Fernet) – encrypted sessions

threading – background scheduler

MySQL

Requests – APIs

Git & GitHub

📂 Project Structure
tkinter_gui_apps/
│
├── app/
│   ├── auth.py
│   ├── session.py
│   ├── crypto.py
│
├── modules/
│   ├── news.py
│   ├── weather.py
│   ├── form.py
│   ├── mail.py
│   ├── scheduler.py
│   ├── smtp_mailer.py
│
├── data/
│   ├── session.json        # ignored in git
│   ├── secret.key          # ignored in git
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

🔐 Gmail SMTP Setup (Important)

Enable 2-Step Verification
https://myaccount.google.com/security

Generate Gmail App Password
https://myaccount.google.com/apppasswords

App: Mail

Device: Other (Tkinter App)

Login in the app using:

Gmail address

App Password (not Gmail password)

▶️ How to Run
1️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run application
python main.py

🔒 Security Notes

Gmail credentials are never stored in plain text

Passwords are encrypted using Fernet

Sensitive files are excluded using .gitignore

🤝 Future Enhancements

Sent Mail History

Inbox Simulation

System Tray Notifications

Packaging as macOS / Windows app

👩‍💻 Author

Manasvi Ghune
Computer Science & IT
Tkinter | Python | Backend | SMTP Automation