# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20141122_2246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='place_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='building',
            name='contents',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='building',
            name='description',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='building',
            name='notes',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
    ]
