# models.py
from django.db import models

class Job(models.Model):
    platforms = (
        ('upwork', 'Upwork'),
        ('kwork', 'Kwork'),
        ('freelancer', 'Freelancer'),
        ('toptal', 'Toptal')
    )
    title = models.CharField(max_length=255)
    url = models.URLField()
    platform = models.CharField(max_length=50, choices=platforms)

    def __str__(self):
        return self.title