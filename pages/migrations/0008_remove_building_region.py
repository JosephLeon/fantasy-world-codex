# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20141130_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='region',
        ),
    ]
