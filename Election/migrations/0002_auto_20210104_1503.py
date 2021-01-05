# Generated by Django 3.1.4 on 2021-01-04 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='endDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='election',
            name='startDate',
            field=models.DateField(),
        ),
    ]