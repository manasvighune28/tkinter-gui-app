from tkinter import messagebox
import threading
import time

def reminder_popup(remind_time):
    def notify():
        while True:
            if time.strftime("%H:%M") == remind_time:
                messagebox.showwarning(
                    "⚠️ Reminder",
                    "Daily report bhejna hai!\nNahi bheja toh salary cut 😡"
                )
                break
            time.sleep(30)

    threading.Thread(target=notify, daemon=True).start()
