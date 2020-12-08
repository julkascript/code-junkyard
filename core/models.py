from django.contrib.auth.models import User
from django.db import models

from accounts.models import UserProfile


class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images', blank=True)
    git_link = models.URLField()
    tags = models.CharField(max_length=100)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.title}"
