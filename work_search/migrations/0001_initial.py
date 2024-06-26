# Generated by Django 5.0.4 on 2024-04-26 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('platform', models.CharField(choices=[('upwork', 'Upwork'), ('kwork', 'Kwork'), ('freelancer', 'Freelancer'), ('toptal', 'Toptal')], max_length=50)),
            ],
        ),
    ]
