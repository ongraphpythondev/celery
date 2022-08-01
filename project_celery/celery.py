from django.conf import settings
import os
from celery import Celery
from celery.schedules import crontab
from pytz import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_celery.settings')

app = Celery('celery_test',)
app.conf.update(timezone = "Asia/Kolkata")

app.config_from_object('django.conf:settings')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'app.tasks.send_mails',
        'schedule': crontab(hour=18, minute=17),
        #'args': (2,)
    }
    
}
app.autodiscover_tasks()