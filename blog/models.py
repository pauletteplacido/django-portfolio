from django.db import models
from datetime import date


class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField(("Date"), default=date.today)

    def __str__(self):
        return self.title
