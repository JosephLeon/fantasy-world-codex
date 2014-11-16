# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20141115_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='place',
            field=models.ForeignKey(blank=True, to='pages.Place', null=True),
            preserve_default=True,
        ),
    ]
