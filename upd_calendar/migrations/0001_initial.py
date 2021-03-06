# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-26 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.IntegerField(default=0)),
                ('date', models.DateField(verbose_name='date deployed')),
                ('run', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kb_name', models.CharField(max_length=50)),
                ('release_date', models.DateField(verbose_name='date released')),
                ('classification', models.PositiveIntegerField(default=0)),
                ('product', models.CharField(max_length=255)),
                ('events', models.ManyToManyField(to='upd_calendar.Event', verbose_name='event')),
            ],
        ),
    ]
