# Generated by Django 3.2.7 on 2024-01-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_dailyduty_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='O', max_length=1),
        ),
        migrations.AddField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, default='N/A', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(default='Employee', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='duty',
            field=models.CharField(default='No Duty Assigned', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(default='John Doe', max_length=100),
        ),
    ]