# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20141116_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_name', models.CharField(max_length=200)),
                ('place', models.ForeignKey(blank=True, to='pages.Place', null=True)),
                ('region', models.ForeignKey(to='pages.Region')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='character',
            name='building',
            field=models.ForeignKey(blank=True, to='pages.Building', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='region',
            field=models.ForeignKey(blank=True, to='pages.Region', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='building',
            field=models.ForeignKey(blank=True, to='pages.Building', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='place',
            field=models.ForeignKey(blank=True, to='pages.Place', null=True),
            preserve_default=True,
        ),
    ]
