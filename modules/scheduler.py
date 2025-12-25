import time
import threading
import datetime
from modules.smtp_mailer import send_mail

def schedule_mail(send_time, subject, body, to_email):
    def worker():
        while True:
            now = datetime.datetime.now().strftime("%H:%M")
            if now == send_time:
                send_mail(subject, body, to_email)
                break
            time.sleep(20)

    threading.Thread(target=worker, daemon=True).start()
