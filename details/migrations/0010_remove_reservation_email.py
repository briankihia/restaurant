# Generated by Django 3.2.7 on 2024-01-26 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0009_auto_20240126_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='email',
        ),
    ]
