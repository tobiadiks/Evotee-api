# Generated by Django 3.1.4 on 2021-01-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('Gender', models.CharField(max_length=1)),
                ('idNumber', models.IntegerField(max_length=13)),
                ('fatherName', models.CharField(max_length=40)),
                ('motherName', models.CharField(max_length=40)),
            ],
        ),
    ]