# Generated by Django 3.2.7 on 2024-01-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0014_alter_employee_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('reservation_date', models.DateField()),
            ],
        ),
    ]
