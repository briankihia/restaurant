# Generated by Django 3.2.7 on 2024-01-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0015_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='phone_number',
            field=models.CharField(blank=True, default='N/A', max_length=15, null=True),
        ),
    ]