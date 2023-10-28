from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.

class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return f"{self.name} {self.url}"


class UserModel(AbstractUser):
    about = models.TextField()
    social_media = models.ManyToManyField(SocialMedia)

    def __str__(self):
        return self.username
