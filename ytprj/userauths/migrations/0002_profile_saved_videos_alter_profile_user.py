# Generated by Django 4.1.7 on 2023-08-24 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_video_featured'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userauths', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='saved_videos',
            field=models.ManyToManyField(blank=True, null=True, related_name='saved_videos', to='core.video'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
