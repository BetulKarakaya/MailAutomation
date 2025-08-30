import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import re
import schedule
import time
import sys

class MailAutomation:
    def __init__(self, sender_email, receiver_email, password, test_mode=True):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.password = password
        self.msg = None
        self.test_mode = test_mode

    def create_mail(self, subject, body):
        self.subject = subject
        self.body = body

    def create_MIME(self):
        self.msg = MIMEMultipart()
        self.msg["From"] = self.sender_email
        self.msg["To"] = self.receiver_email
        self.msg["Subject"] = self.subject
        self.msg.attach(MIMEText(self.body, "plain"))

    def SMTPLIB_connection(self):
        server = None
        try:
            if self.test_mode:
                server = smtplib.SMTP("localhost", 1025)
            else:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(self.sender_email, self.password)

            server.sendmail(self.sender_email, self.receiver_email, self.msg.as_string())
            print("✅ Email was sent successfully!")
        except Exception as e:
            print("❌ An error occurred, the email could not be sent!:", e)
        finally:
            if server:
                server.quit()
            sys.exit("Mail sent, shutting down program.")

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def main():
    print("---Gmail Mail Automation---")
    test_mode = input("Test mode? (y/n): ").strip().lower() == "y"

    sender_email = input("Enter your Gmail address: ").strip()
    while not is_valid_email(sender_email):
        print("⚠️ Invalid email format! Please try again.")
        sender_email = input("Enter your Gmail address: ").strip()

    receiver_email = input("Enter receiver's email address: ").strip()
    while not is_valid_email(receiver_email):
        print("⚠️ Invalid email format! Please try again.")
        receiver_email = input("Enter receiver's email address: ").strip()

    password = None
    if not test_mode:
        password = getpass.getpass("Enter your Gmail App Password (hidden): ")

    subject = input("Enter subject: ").strip()
    body = input("Enter email body: ").strip()

    automation = MailAutomation(sender_email, receiver_email, password, test_mode=test_mode)
    automation.create_mail(subject=subject, body=body)
    automation.create_MIME()

    # Ask user for schedule
    schedule_choice = input("Do you want to schedule this email? (y/n): ").strip().lower()
    if schedule_choice == "y":
        send_time = input("Enter time (HH:MM, 24h format): ").strip()
        try:
            schedule.every().day.at(send_time).do(automation.SMTPLIB_connection)
            print(f"Email scheduled at {send_time}. Waiting...")
            while True:
                schedule.run_pending()
                time.sleep(1)
        except Exception as e:
            print("⚠️ Invalid time format or scheduling error:", e)
    else:
        automation.SMTPLIB_connection()

if __name__ == "__main__":
    main()
