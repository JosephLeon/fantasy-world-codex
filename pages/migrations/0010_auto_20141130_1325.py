# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20141130_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='character_name',
            new_name='name',
        ),
    ]
