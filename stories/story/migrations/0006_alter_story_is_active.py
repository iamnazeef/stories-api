# Generated by Django 5.1.3 on 2024-11-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0005_alter_story_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
