# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='other_location',
            field=models.ForeignKey(blank=True, to='pages.Location', null=True),
            preserve_default=True,
        ),
    ]
