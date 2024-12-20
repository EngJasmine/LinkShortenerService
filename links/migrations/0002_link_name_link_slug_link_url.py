# Generated by Django 5.1.3 on 2024-11-25 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='name',
            field=models.CharField(default=' ', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='link',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='link',
            name='url',
            field=models.URLField(default=' '),
        ),
    ]
