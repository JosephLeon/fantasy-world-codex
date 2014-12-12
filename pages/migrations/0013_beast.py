# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20141130_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('treasure', models.TextField(blank=True)),
                ('attack', models.IntegerField(default=12)),
                ('defense', models.IntegerField(default=12)),
                ('damage', models.IntegerField(default=12)),
                ('strength', models.IntegerField(default=12)),
                ('stamina', models.IntegerField(default=12)),
                ('speed', models.IntegerField(default=12)),
                ('agility', models.IntegerField(default=12)),
                ('toughness', models.IntegerField(default=12)),
                ('constitution', models.IntegerField(default=12)),
                ('intelligence', models.IntegerField(default=12)),
                ('logic', models.IntegerField(default=12)),
                ('teaching', models.IntegerField(default=12)),
                ('intuition', models.IntegerField(default=12)),
                ('beauty', models.IntegerField(default=12)),
                ('charisma', models.IntegerField(default=12)),
                ('leadership', models.IntegerField(default=12)),
                ('item', models.ForeignKey(blank=True, to='pages.Item', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
