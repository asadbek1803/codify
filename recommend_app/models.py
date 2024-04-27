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
