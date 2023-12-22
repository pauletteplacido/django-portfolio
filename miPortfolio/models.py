from django.db import models
from django.db.models.fields import URLField
from datetime import date


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    date = models.DateField(("Date"), default=date.today)

    def __str__(self):
        return self.title
