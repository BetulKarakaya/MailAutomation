# MailAutomation

A Python script for **automated email sending**.  

> **Why use a local debug server?**  
> The local debug server allows you to **test email sending safely** without actually sending emails to real recipients.  
> It prints email content to the console, so you can verify formatting, subject, and body before using a real Gmail account.  
> This prevents accidental spam or sending test emails to someone by mistake.

Supports both **local debug server** testing (no real emails sent) and **real Gmail SMTP** sending.

---

## Features

- Compose email **subject** and **body**
- Send emails via **Gmail SMTP** with App Password
- **Local debug server** for safe testing
- **Email format validation** for sender and receiver

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

## Local Debug Server (Optional for Testing)
Start the debug SMTP server:
```bash
python debug_server.py
```
    -Runs on localhost:1025.
    -All sent emails are printed to the console.
    -Does not send emails to real recipients.

## Usage
Test Mode (Local Debug Server)
```bash
python automation.py
```
When prompted:
```bash
Test mode? (y/n): y
```
The script will use the local debug server.

Real Gmail Mode
```bash
python automation.py
```
When prompted:
```bash
Test mode? (y/n): n
```
    -Enter your Gmail App Password when asked.
    -Uses Gmail SMTP (smtp.gmail.com:587) with STARTTLS.

## Notes
- Test mode disables STARTTLS and login() because the debug server does not support authentication.

- Always use a Gmail App Password for real Gmail sending.

- Make sure sender and receiver emails are valid; the script will prompt until a correct format is entered.

## Example
Start debug server in one terminal:

```bash
python debug_server.py
```
Run automation script in another terminal:

```bash
python automation.py
```
Enter sender, receiver, subject, and body.
Check the debug server terminal for the printed email details.
