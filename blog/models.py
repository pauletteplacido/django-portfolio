from django.db import models
from datetime import date


class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    media_file = models.FileField(
        upload_to='blog/media/', null=True, blank=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title
