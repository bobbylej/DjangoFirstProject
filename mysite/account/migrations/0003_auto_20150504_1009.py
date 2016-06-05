# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150504_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='equipment',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='gym',
        ),
        migrations.AddField(
            model_name='equipment',
            name='photos',
            field=models.ManyToManyField(default=None, to='account.Photo', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gym',
            name='photos',
            field=models.ManyToManyField(default=None, to='account.Photo', null=True, blank=True),
            preserve_default=True,
        ),
    ]
