# Generated by Django 5.0.4 on 2024-04-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('upwork', 'Upwork'), ('kwork', 'Kwork'), ('toptal', 'Toptal')], max_length=20)),
                ('is_recommend', models.BooleanField(default=False)),
            ],
        ),
    ]
