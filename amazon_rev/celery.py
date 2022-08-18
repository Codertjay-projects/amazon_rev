import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon_rev.settings')

# used redis broker if it exists
app = Celery('amazon_rev', broker="redis://localhost:6379", backend="redis://localhost:6379")

app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)
BROKER_URL = "redis://localhost:6379"
broker_url = "redis://localhost:6379"
app.conf.broker_url = BROKER_URL
CELERY_BROKER_URL = BROKER_URL

app.conf.beat_schedule = {

    'send_admin_message': {
        'task': 'core.tasks.run_automation_bot',
        'schedule': 350000000,
    },
}


@app.task
def debug_task():
    print(f'Request: ')
