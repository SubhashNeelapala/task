# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='fifties',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='highest_scores',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='hundreds',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='matches',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='runs',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_jersey_no',
            field=models.CharField(default=1, unique=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default=1, unique=True, max_length=100),
            preserve_default=False,
        ),
    ]
