from django.db import models

# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=50)
    base_file = models.FileField(upload_to='apps/apk/')

    def __str__(self):
        return self.name