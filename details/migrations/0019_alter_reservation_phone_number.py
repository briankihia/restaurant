# Generated by Django 3.2.7 on 2024-01-26 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0018_alter_reservation_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]