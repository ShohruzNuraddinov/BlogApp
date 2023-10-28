import datetime

from django.db import models
from users.models import UserModel
import readtime

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)
    # readed_time = models.TimeField()
    # comments = models.ManyToManyField(Comment)

    @property
    def read_time(self):
        result = readtime.of_text(self.content)
        return result.text

    def __str__(self):
        return self.title
