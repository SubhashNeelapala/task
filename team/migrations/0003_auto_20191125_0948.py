# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20191125_0947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='fifties',
            new_name='no_fifties',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='hundreds',
            new_name='no_hundreds',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='matches',
            new_name='no_matches',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='runs',
            new_name='no_runs',
        ),
    ]
