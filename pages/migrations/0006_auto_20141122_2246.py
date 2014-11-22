# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20141122_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='place_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='place',
            name='description',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='economy',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='population',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='special_features',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
    ]
