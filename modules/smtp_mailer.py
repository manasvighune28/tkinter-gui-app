import smtplib
from email.message import EmailMessage
from app.session import load_session

def send_mail(subject, body, to_email):
    sender_email, app_password = load_session()

    if not sender_email or not app_password:
        raise Exception("Not logged in")

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
            print("✅ Mail sent successfully")

    except Exception as e:
        print("❌ SMTP ERROR:", e)
