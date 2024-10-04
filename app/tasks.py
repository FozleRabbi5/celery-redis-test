from app.celery_app import celery_app
from app.mailing_system.mail_sending import celery_send_mail
from pydantic import EmailStr

# Example of a simple task
@celery_app.task(name="app.tasks.add_numbers")
def add_numbers(x: int, y: int) -> int:
    return x + y

# Example of a scheduled task
@celery_app.task(name="app.tasks.scheduled_task")
def scheduled_task():
    print("This is a scheduled task running periodically")

@celery_app.task(name="app.tasks._send_email")
def _send_email(to_email: EmailStr, subject: str, body: str):
    response = celery_send_mail(to_email=to_email, subject=subject, body=body)
    return response

@celery_app.task(name="app.tasks.check_elevate_forms")
def check_elevate_forms():
    print("This is a scheduled task running periodically")
    return True
