# Generated by Django 3.1.4 on 2021-01-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voters', '0002_voter_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='id',
            field=models.IntegerField(default=0),
        ),
    ]
