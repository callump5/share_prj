# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-01 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20180501_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_details',
            name='staff_image',
            field=models.ImageField(default='', upload_to=gallery.models.upload_staff_img),
            preserve_default=False,
        ),
    ]
