# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upd_calendar', '0006_auto_20160507_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='product',
            field=models.CharField(choices=[('w7', 'windows 7'), ('w10', 'windows 10'), ('o10', 'office 10'), ('o13', 'office 13'), ('oth', 'other product')], max_length=4),
        ),
    ]
