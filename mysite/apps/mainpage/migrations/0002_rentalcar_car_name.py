# Generated by Django 3.0.2 on 2020-05-19 13:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalcar',
            name='car_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Название машины'),
            preserve_default=False,
        ),
    ]
