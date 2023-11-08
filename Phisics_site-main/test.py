import smtplib
import os
from email.mime.text import MIMEText


def send_email(message):
    sender = "d.chenchenko@student.univers.su"
    password = "Distant12357"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "CLICK ME PLEASE!"
        server.sendmail(sender, sender, msg.as_string())

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    message = input("Type your message: ")
    print(send_email(message=message))


if __name__ == "__main__":
    main()