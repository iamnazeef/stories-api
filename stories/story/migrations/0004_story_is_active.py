# Generated by Django 5.1.3 on 2024-11-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_story_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]