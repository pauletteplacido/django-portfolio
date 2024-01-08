from django.db import models
from django.db.models.fields import URLField
from datetime import date


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    media_file = models.FileField(
        upload_to='portfolio/media/', null=True, blank=True)
    url = models.URLField(blank=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=100, blank=True)
    body = models.CharField(max_length=250, blank=True)
    background_image = models.ImageField(upload_to='backgrounds/images/')
    url = models.URLField(blank=True)
    date = models.DateField(("Date"), default=date.today)

    def __str__(self):
        return self.title


class Profile(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    date = models.DateField(("Date"), default=date.today)

    def __str__(self):
        return self.title
