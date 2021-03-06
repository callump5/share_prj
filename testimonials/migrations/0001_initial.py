# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-18 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('content', tinymce.models.HTMLField(max_length=500)),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='review_status', to='testimonials.Status')),
            ],
        ),
    ]
