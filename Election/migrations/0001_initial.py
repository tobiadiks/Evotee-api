# Generated by Django 3.1.4 on 2021-01-01 09:25

import Election.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electionName', models.CharField(max_length=200)),
                ('electionId', models.IntegerField(default=Election.models.generator, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.electorate')),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VoterId', models.IntegerField(default=Election.models.generator)),
                ('is_active', models.BooleanField(default=True)),
                ('electionVoted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Election.election')),
            ],
        ),
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contestantName', models.CharField(default='', max_length=30)),
                ('position', models.CharField(default='', max_length=40)),
                ('votes', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('electionName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Election.election')),
            ],
        ),
    ]
