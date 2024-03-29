# Generated by Django 3.1.4 on 2021-01-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Election', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('firstName', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('Gender', models.CharField(max_length=1)),
                ('idNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('fatherName', models.CharField(max_length=40)),
                ('motherName', models.CharField(max_length=40)),
                ('active', models.BooleanField(default=True)),
                ('voted', models.BooleanField(default=False)),
                ('qualifiedElection', models.ManyToManyField(to='Election.Election')),
            ],
        ),
    ]
