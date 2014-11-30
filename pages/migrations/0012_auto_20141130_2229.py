# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20141130_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='effects',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.CharField(default=b'Ring', max_length=255, choices=[(b'Ring', b'Ring'), (b'Staff', b'Staff'), (b'Weapon', b'Weapon'), (b'Hat', b'Hat'), (b'Necklace', b'Necklace'), (b'Earring', b'Earring'), (b'Shirt', b'Shirt'), (b'Cloak', b'Cloak'), (b'Belt', b'Belt'), (b'Pants', b'Pants'), (b'Gloves', b'Gloves'), (b'Boots', b'Boots'), (b'Miscellaneous', b'Miscellaneous')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='character',
            field=models.ForeignKey(blank=True, to='pages.Character', null=True),
            preserve_default=True,
        ),
    ]
