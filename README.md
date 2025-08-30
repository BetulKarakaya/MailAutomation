# MailAutomation

A Python script for **automated email sending**.  

> **Why use a local debug server?**  
> The local debug server allows you to **test email sending safely** without actually sending emails to real recipients.  
> It prints email content to the console, so you can verify formatting, subject, and body before using a real Gmail account.  
> This prevents accidental spam or sending test emails to someone by mistake.

Supports both **local debug server** testing (no real emails sent) and **real Gmail SMTP** sending.

---

## 🚀 Features

- Create and customize email **subject** and **body**.
- Send emails via **Gmail SMTP** (normal mode).
- Test email sending safely using a **local debug server** without sending real emails (debug/test mode).
- Schedule emails for automatic sending using `schedule`.

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/BetulKarakaya/MailAutomation
cd smtplib_mail_automation_github
```


2. Install dependencies:

```bash
pip install aiosmtpd
```

```bash
pip install schedule
```

Usage
1. Normal Mode (Send Real Emails)
``` python
from mail_automation import MailAutomation

sender = "your_email@gmail.com"
receiver = "receiver_email@gmail.com"
password = "your_password"  # use getpass for security

# Normal mode sends real emails via Gmail SMTP
mail_bot = MailAutomation(sender, receiver, password, test_mode=False)
mail_bot.send_email(subject="Hello", body="This is a real email!")
```
2. Debug/Test Server Mode
``` python
from mail_automation import MailAutomation

sender = "your_email@gmail.com"
receiver = "receiver_email@gmail.com"
password = "your_password"

# Test mode prints email content to console without sending
mail_bot = MailAutomation(sender, receiver, password, test_mode=True)
mail_bot.send_email(subject="Test Email", body="This email will not be sent.")
```
✅ Debug mode is safe for testing formatting and content without sending real emails.

3. Scheduling Emails
``` python
import schedule
import time

# Schedule a daily email at 09:00
schedule.every().day.at("09:00").do(
    mail_bot.send_email, subject="Daily Report", body="Here is your daily report."
)

while True:
    schedule.run_pending()
    time.sleep(60)
```
🔒 Security Tips
- Avoid storing passwords in plain text.
- Use app passwords for Gmail if 2FA is enabled.
- Consider using Python's getpass module to securely input passwords.

📂 File Structure
```bash
MailAutomation/
│
├─ mail_automation.py  # Main automation script
├─ README.md           # This file
└─ requirements.txt    # Optional: required modules
```
✅ License
This project is licensed under the MIT License.
