# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='place',
        ),
        migrations.RemoveField(
            model_name='building',
            name='region',
        ),
        migrations.RemoveField(
            model_name='character',
            name='building',
        ),
        migrations.RemoveField(
            model_name='item',
            name='building',
        ),
        migrations.DeleteModel(
            name='Building',
        ),
    ]
