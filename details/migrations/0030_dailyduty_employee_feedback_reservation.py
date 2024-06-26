# Generated by Django 3.2.7 on 2024-01-27 13:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0029_auto_20240127_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='John Doe', max_length=100)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, default='N/A', max_length=15, null=True)),
                ('position', models.CharField(default='Employee', max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='O', max_length=1)),
                ('hire_date', models.DateField(default='2000-01-01')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='N/A', max_length=100)),
                ('email', models.EmailField(default='example@example.com', max_length=254)),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='example@example.com', max_length=254)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('number_of_guests', models.PositiveIntegerField(default='1', validators=[django.core.validators.MaxValueValidator(10)])),
                ('special_request', models.TextField(blank=True, null=True)),
                ('reservation_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DailyDuty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('duty', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.employee')),
            ],
        ),
    ]
