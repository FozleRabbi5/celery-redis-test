from dotenv import load_dotenv
import os

load_dotenv()


ses_smtp_server = os.getenv("SES_SMTP_SERVER")
ses_smtp_port = os.getenv("SES_SMTP_PORT")
ses_email = os.getenv("SES_EMAIL")
ses_smtp_username = os.getenv("SES_SMTP_USERNAME")
ses_smtp_password = os.getenv("SES_SMTP_PASSWORD")

rabbitmq_url = os.getenv("RABBITMQ_URL")
redis_url = os.getenv("REDIS_URL")
