# Generated by Django 5.2 on 2025-04-07 16:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quora', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='quorapost',
            name='likes',
            field=models.ManyToManyField(blank=True, help_text='Users who liked this post.', related_name='liked_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
