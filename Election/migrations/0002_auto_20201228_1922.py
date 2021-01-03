# Generated by Django 3.1.4 on 2020-12-28 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='contestantName',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='electionName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Election.election'),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='position',
            field=models.CharField(default='', max_length=40),
        ),
    ]