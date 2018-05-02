# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
import os
from django.utils.timezone import now

# Create your models here.



def upload_staff_img(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'staff/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )



class Info_Content(models.Model):

    info = HTMLField()

    def __unicode__(self):

        return 'info'


class Sticky_Note(models.Model):

    title = models.CharField(max_length= 50)

    content = models.CharField(max_length=300)

    img = models.ImageField(upload_to=upload_staff_img, null=True, blank=True)

    def __unicode__(self):
        return self.title





class Sponsers(models.Model):
    company = models.CharField(max_length=200)
    img = models.ImageField(upload_to=upload_staff_img)

    def __unicode__(self):
        return self.company