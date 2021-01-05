# Generated by Django 3.1.4 on 2021-01-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestant',
            name='id',
        ),
        migrations.AddField(
            model_name='contestant',
            name='contestantId',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
