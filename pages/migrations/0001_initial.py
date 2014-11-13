# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character_name', models.CharField(max_length=200)),
                ('building', models.ForeignKey(to='pages.Building')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=200)),
                ('building', models.ForeignKey(to='pages.Building')),
                ('character', models.ForeignKey(to='pages.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='place',
            name='region',
            field=models.ForeignKey(to='pages.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='place',
            field=models.ForeignKey(to='pages.Place'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='place',
            field=models.ForeignKey(to='pages.Place'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='place',
            field=models.ForeignKey(to='pages.Place'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='region',
            field=models.ForeignKey(to='pages.Region'),
            preserve_default=True,
        ),
    ]
