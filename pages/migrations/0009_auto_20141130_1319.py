# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_remove_building_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='agility',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='beauty',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='charisma',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='constitution',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='intuition',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='leadership',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='logic',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.CharField(default=b'Human', max_length=255, choices=[(b'Human', b'Human'), (b'Dwarf', b'Dwarf'), (b'Elf', b'Elf'), (b'Halfling', b'Halfling'), (b'Human/Dwarf', b'Human/Dwarf'), (b'Human/Elf', b'Human/Elf'), (b'Human/Halfling', b'Human/Halfling'), (b'Dwarf/Elf', b'Dwarf/Elf'), (b'Dwarf/Halfling', b'Dwarf/Halfling'), (b'Elf/Halfling', b'Elf/Halfling'), (b'Gunder', b'Gunder'), (b'Orc', b'Orc'), (b'Goblin', b'Goblin'), (b'Human/Orc', b'Human/Orc'), (b'Dwarf/Orc', b'Dwarf/Orc'), (b'Elf/Orc', b'Elf/Orc')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='speed',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='stamina',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='teaching',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='toughness',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='building',
            name='place',
            field=models.ForeignKey(default='', to='pages.Place'),
            preserve_default=False,
        ),
    ]
