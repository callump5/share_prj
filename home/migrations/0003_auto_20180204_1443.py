# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-04 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180204_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='status',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
    ]
