from celery import shared_task
from django.db import transaction

from main.models import Notification


@shared_task
def notification_status(pk):
    with transaction.atomic():
        notifi = Notification.objects.select_for_update().get(id=pk)
        notifi.status = True
        notifi.save()

    return 'Notification read'