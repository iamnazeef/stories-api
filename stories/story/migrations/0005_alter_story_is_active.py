# Generated by Django 5.1.3 on 2024-11-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_story_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
