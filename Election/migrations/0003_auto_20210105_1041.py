# Generated by Django 3.1.4 on 2021-01-05 09:41

import Election.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0002_auto_20210105_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='contestantId',
            field=models.IntegerField(default=Election.models.generator, primary_key=True, serialize=False),
        ),
    ]