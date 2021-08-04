from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    body = models.TextField()
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name="replies", null=True)

    def __str__(self):
        return self.name
