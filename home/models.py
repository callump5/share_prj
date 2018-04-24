# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import os
from django.utils.timezone import now
# Create your models here.


def upload_staff_img(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'staff/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )


class SlideImage(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to=upload_staff_img, blank=True, null=True)

    def __unicode__(self):
        return self.name