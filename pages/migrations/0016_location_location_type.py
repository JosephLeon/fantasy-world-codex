# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20141217_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='location_type',
            field=models.CharField(default=b'Continent', max_length=255, choices=[(b'Universe', b'Universe'), (b'Planet', b'Planet'), (b'Continent', b'Continent'), (b'Region', b'Region'), (b'Country', b'Country'), (b'Province', b'Province'), (b'City', b'City'), (b'Area', b'Area'), (b'Building', b'Building')]),
            preserve_default=True,
        ),
    ]
