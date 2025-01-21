# Generated by Django 5.0.6 on 2024-06-12 16:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
