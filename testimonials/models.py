# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from tinymce.models import HTMLField

# Create your models here.

class Status(models.Model):
    status = models.CharField(max_length=100)

    def __unicode__(self):
        return self.status

class Testimonial(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='Anonymous')
    content = HTMLField()
    status = models.ForeignKey(Status, related_name='review_status', default=1)

    def __unicode__(self):
        return self.title