# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Status(models.Model):
    status = models.CharField(max_length=200)

    def __unicode__(self):
        return self.status

class Contact_Info(models.Model):

    status = models.ForeignKey(Status, related_name='contact_status', default=1)
    name = models.CharField(max_length=300)
    number = models.CharField(max_length=10)
    email = models.CharField(max_length=200)

    text = HTMLField()

    def __unicode__(self):
        return self.name