# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=100, null=True, blank=True)),
                ('lastname', models.CharField(max_length=100, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'Player', blank=True)),
                ('player_jersey_no', models.CharField(max_length=100, null=True, blank=True)),
                ('country', models.CharField(max_length=100, null=True, blank=True)),
                ('player_history', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, unique=True, null=True, blank=True)),
                ('logo', models.ImageField(null=True, upload_to=b'Team', blank=True)),
                ('club_state', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='player_team',
            field=models.ForeignKey(blank=True, to='team.Team', null=True),
        ),
    ]
