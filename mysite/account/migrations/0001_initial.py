# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('desc', models.CharField(default=None, max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Addition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientsVoucher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_order', models.DateField()),
                ('date_end', models.DateField()),
                ('client', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('city', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=6)),
                ('street', models.CharField(max_length=30)),
                ('no_building', models.CharField(max_length=6)),
                ('no_local', models.CharField(default=None, max_length=6, null=True, blank=True)),
                ('open_time', models.TimeField(default=None, null=True, blank=True)),
                ('close_time', models.TimeField(default=None, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GymActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('max_people', models.PositiveIntegerField(default=None, null=True, blank=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('activity', models.ForeignKey(to='account.Activity')),
                ('clients', models.ManyToManyField(default=None, related_name='client_gym_activity', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('gym', models.ForeignKey(to='account.Gym')),
                ('instructor', models.ForeignKey(related_name='employee_gym_activity', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('desc', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('price', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('days', models.PositiveIntegerField(default=30, validators=[django.core.validators.MinValueValidator(0)])),
                ('additions', models.ManyToManyField(default=None, to='account.Addition', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='clientsvoucher',
            name='voucher',
            field=models.ForeignKey(to='account.Voucher'),
            preserve_default=True,
        ),
    ]
