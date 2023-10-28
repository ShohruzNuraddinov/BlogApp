from django.db import models
from users.models import UserModel
from post.models import Post

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self) -> str:
        return self.user.username + ' write: ' + self.content
