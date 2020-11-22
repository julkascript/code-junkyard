from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images')
    tags = models.CharField(max_length=100)



