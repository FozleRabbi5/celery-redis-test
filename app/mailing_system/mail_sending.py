import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

from pydantic import EmailStr

from app.configuration.config import ses_smtp_password, ses_smtp_username, ses_smtp_port, ses_smtp_server, ses_email






def celery_send_mail(to_email: EmailStr, subject: str, body: str):
    # Create the message
    message = MIMEMultipart()
    message["From"] = ses_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))

    # Connect to the SES SMTP server
    try:
        with smtplib.SMTP(ses_smtp_server, ses_smtp_port) as server:
            server.starttls()  # Use if your SES SMTP server requires a secure connection
            server.login(ses_smtp_username, ses_smtp_password)
            server.sendmail(ses_email, to_email, message.as_string())
        return {"success": True, "message": "Email sent successfully!"}
    except Exception as e:
        return {"success": False, "message": f"Failed to send email. Error: {str(e)}"}