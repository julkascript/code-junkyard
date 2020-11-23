from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images')
    git_link = models.URLField()
    tags = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.title}"
