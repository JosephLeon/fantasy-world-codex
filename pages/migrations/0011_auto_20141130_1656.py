# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20141130_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='character_class',
            field=models.CharField(default=b'Fighter', max_length=255, choices=[(b'Fighter', b'Fighter'), (b'Thief', b'Thief'), (b'Survivalist', b'Survivalist'), (b'Cleric', b'Cleric'), (b'Mage', b'Mage'), (b'Mentalist', b'Mentalist'), (b'Fighter/Thief', b'Fighter/Thief'), (b'Fighter/Survivalist', b'Fighter/Survivalist'), (b'Fighter/Cleric', b'Fighter/Cleric'), (b'Fighter/Mage', b'Fighter/Mage'), (b'Fighter/Mentalist', b'Fighter/Mentalist'), (b'Thief/Survivalist', b'Thief/Survivalist'), (b'Thief/Cleric', b'Thief/Cleric'), (b'Thief/Mage', b'Thief/Mage'), (b'Thief/Mentalist', b'Thief/Mentalist'), (b'Survivalist/Cleric', b'Survivalist/Cleric'), (b'Survivalist/Mage', b'Survivalist/Mage'), (b'Survivalist/Mentalist', b'Survivalist/Mentalist'), (b'Cleric/Mage', b'Cleric/Mage'), (b'Cleric/Mentalist', b'Cleric/Mentalist'), (b'Mage/Mentalist', b'Mage/Mentalist')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='color',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='description',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='gold',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='height',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='skills',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='weight',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
