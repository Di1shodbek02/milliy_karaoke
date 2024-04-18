import secrets
from http.client import HTTPException

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponseBadRequest
from .models import Video, UserPersonalize, Notification, Category

import logging

User = get_user_model()

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Video)
def create_special_notification(instance, created):
    if created:
        try:
            user_profile = User.objects.get(username=instance.category_id.name)
            if user_profile.username == instance.category_id.name:
                user_profiles = UserPersonalize.objects.filter(personalize=instance.category_id)
            for user_profile in user_profiles:
                user = user_profile.user_id

                Notification.objects.create(
                    user_id=user,
                    title="Special Notification For You 📩",
                    text=f"A new book in your personalized category '{instance.category_id.name.upper()}' has been added: {instance.name}",
                    status=False
                )
        except ObjectDoesNotExist:
            return HttpResponseBadRequest('Error Occurred')


@receiver(post_save, sender=Video)
def update_hashcode_for_audio(instance, created, **kwargs):
    if created:
        try:
            video = Video.objects.select_for_update().get(pk=instance.id)
            hashcode = secrets.token_hex(32)
            video.hashcode = hashcode
            video.save()
        except Exception as e:
            logger.error("Error updating hashcode for video: %s", e)


@receiver(post_save, sender=Category)
def update_hashcode_for_audio(instance, created):
    if created:
        try:
            category = Category.objects.select_for_update().get(pk=instance.id)
            hashcode = secrets.token_hex(32)
            category.hashcode = hashcode
            category.save()

        except Exception as e:
            raise HTTPException(status_code=400, detail=e)
        return {'success': True, 'message': 'Hashcode Created Successfully'}
