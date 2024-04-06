from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='pics', blank=True, null=True)
    phone = models.CharField(unique=True, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.role.name
