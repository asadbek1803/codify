from django.db import models

# Create your models here.
class SiteSettings(models.Model):
    little_title = models.CharField(max_length=200)
    big_title = models.CharField(max_length=150)
    description = models.TextField()
    link_site = models.URLField(blank=True, null=True)
    link_name = models.CharField(max_length=80)
    video = models.FileField(upload_to='welcome/videos/', blank=True, null=True)
    whats_video = models.CharField(max_length=150)

    def __str__(self):
        return self.big_title



class Platforms(models.Model):
    name = models.CharField(max_length=80)
    about = models.TextField()
    image = models.ImageField(upload_to='platforms/images/')
    blog_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class AboutUsQuestions(models.Model):
    question = models.TextField()
    answer = models.TextField()
    class_name = models.CharField(max_length=150, blank=True, null=True)


    def __str__(self):
        return self.question


class SiteUsersAbout(models.Model):
    students = models.SmallIntegerField()
    total_courses = models.SmallIntegerField()
    finished_courses = models.SmallIntegerField()

class Team(models.Model):
    work = models.CharField(max_length=80)
    full_name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='profiles/images/team/', null=True, blank=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name




