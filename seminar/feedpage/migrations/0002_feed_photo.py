# Generated by Django 3.0.5 on 2020-05-30 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='photo',
            field=models.ImageField(blank=True, upload_to='feed_photos'),
        ),
    ]
