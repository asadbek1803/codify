from django.db import models

# Create your models here.
class Apps(models.Model):
    platforms = (
        ('upwork', 'Upwork'),
        ('kwork', 'Kwork'),
        ('toptal', 'Toptal')

    )
    name = models.CharField(max_length=20, choices=platforms)
    is_recommend = models.BooleanField(default=False)



    def __str__(self):
        return self.name


class PlatformsLessons(models.Model):
    categorys = (
        ('upwork', 'upwork'),
        ('kwork', 'kwork'),
        ('toptal', 'toptal')
    )
    dars_title = models.CharField(max_length=80)
    youtube_logo = models.ImageField(upload_to='youtube/images/')
    category = models.CharField(max_length=25, choices=categorys)
    author = models.CharField(max_length=75)
    youtube_link = models.URLField()

    def __str__(self):
        return self.dars_title




