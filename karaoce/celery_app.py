import os

from celery import Celery

app = Celery('karaoce')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'karaoce.settings')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
