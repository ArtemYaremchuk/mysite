# Generated by Django 3.0.2 on 2020-03-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=90, verbose_name='Название машины')),
                ('car_pic', models.CharField(max_length=100, verbose_name='Картинки')),
                ('doors', models.IntegerField(verbose_name='Количество дверей')),
                ('petrol', models.FloatField(verbose_name='Бензин на 100км')),
                ('luggage', models.IntegerField(verbose_name='Багаж')),
                ('price26', models.IntegerField(max_length=20, verbose_name='цена на 26 суток')),
                ('price10', models.IntegerField(max_length=20, verbose_name='цена на 10-25 суток')),
                ('price4', models.IntegerField(max_length=20, verbose_name='цена на 4-9 суток')),
                ('price1', models.IntegerField(max_length=20, verbose_name='цена на 1-3 суток')),
            ],
        ),
    ]