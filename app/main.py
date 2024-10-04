from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from app.tasks import _send_email, check_elevate_forms

app = FastAPI()

class EmailRequest(BaseModel):
    to_email: EmailStr
    subject: str
    body: str

@app.post("/send-email/")
async def send_email(email_request: EmailRequest):
    try:
        task = _send_email.apply_async(
            args=[email_request.to_email, email_request.subject, email_request.body],
            countdown=300  # Delay task for 5 minutes (300 seconds)
        )
        now = datetime.now()
        print(now)
        # task = check_elevate_forms.apply_async(
        #     countdown=60
        # )
        print(task)
        return {"message": "Email is being sent", "task_id": task.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "FastAPI with Celery is running"}
