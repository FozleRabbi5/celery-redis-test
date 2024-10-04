from celery import Celery
from app.configuration.config import redis_url, rabbitmq_url

# Configure Celery to use RabbitMQ as the message broker and Redis as the result backend
celery_app = Celery(
    "tasks",
    broker=rabbitmq_url,
    backend=redis_url,
    include=['app.tasks']  # Explicitly include your task module here
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    broker_connection_retry_on_startup=True
)

# Autodiscover tasks in the 'app' module
celery_app.autodiscover_tasks(['app'])

celery_app.conf.beat_schedule = {
    'check_elevate_forms_every_hour': {
        'task': 'app.tasks.check_elevate_forms',
        'schedule': 10.0,  # 1 hour
    },
}
