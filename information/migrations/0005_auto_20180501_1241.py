# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-01 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import information.models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_auto_20180501_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsers',
            name='img',
            field=models.ImageField(default=' ', upload_to=information.models.upload_staff_img),
            preserve_default=False,
        ),
    ]
