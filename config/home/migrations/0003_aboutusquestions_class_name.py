# Generated by Django 5.0.4 on 2024-04-27 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_aboutusquestions_platforms_siteusersabout_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutusquestions',
            name='class_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
