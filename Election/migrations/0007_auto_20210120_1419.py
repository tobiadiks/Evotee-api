# Generated by Django 3.1.4 on 2021-01-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0006_election_enddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='contestantName',
            field=models.CharField(max_length=64),
        ),
    ]
