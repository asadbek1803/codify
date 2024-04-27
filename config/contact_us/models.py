from django.db import models
from accounts.models import Account

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=90)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.full_name


class RateUs(models.Model):
    rating_stars = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')
    )
    full_name = models.CharField(max_length=80)
    working = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='images/rating/', blank=True, null=True)
    rate = models.CharField(max_length=18, choices=rating_stars)
    description = models.TextField()

    def __str__(self):
        return self.full_name




