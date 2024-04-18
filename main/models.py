from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.db import models

from accounts.models import User


class Category(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    music = models.FileField(upload_to='music/')
    text = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LikeVideo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('video_id', 'user_id')

    def __str__(self):
        return f'LikeCount for Video {self.video_id_id} by User {self.user_id_id}'


class Basket(models.Model):
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('video_id', 'user_id')


class Comment(models.Model):
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class UserPersonalize(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    personalize = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class UserPersonalizez_personalize(models.Model):
    user_personalize = models.ForeignKey(UserPersonalize, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        pass
