# Generated by Django 3.1.4 on 2021-01-04 10:52

import Election.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('electionName', models.CharField(max_length=200)),
                ('electionId', models.IntegerField(default=Election.models.generator, primary_key=True, serialize=False, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('startDate', models.DateField(default=django.utils.timezone.now)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.electorate')),
            ],
        ),
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contestantName', models.CharField(default='', max_length=30)),
                ('position', models.CharField(default='', max_length=40)),
                ('votes', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('electionName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Election.election')),
            ],
        ),
    ]
