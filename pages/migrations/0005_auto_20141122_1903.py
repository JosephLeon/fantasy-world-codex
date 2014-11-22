# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20141116_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='region',
            old_name='region_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='region',
            name='description',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
    ]
