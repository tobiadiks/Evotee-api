# Generated by Django 3.1.4 on 2021-01-04 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
