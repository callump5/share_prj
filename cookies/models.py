# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Cookies(models.Model):
    name = models.CharField(max_length=200)
    desription = HTMLField()

    def __unicode__(self):
        return self.name