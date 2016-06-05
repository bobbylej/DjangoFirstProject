# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('desc', models.CharField(default=None, max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('name', models.CharField(max_length=50, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('link', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('equipment', models.ForeignKey(default=None, blank=True, to='account.Equipment', null=True)),
                ('gym', models.ForeignKey(default=None, blank=True, to='account.Gym', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='equipment',
            name='muscles',
            field=models.ManyToManyField(default=None, to='account.Muscle', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gym',
            name='equipments',
            field=models.ManyToManyField(default=None, to='account.Equipment', null=True, blank=True),
            preserve_default=True,
        ),
    ]
