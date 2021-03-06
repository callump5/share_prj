# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
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


class Staff_Details(models.Model):

    user = models.ForeignKey(User, related_name='staff_profile')
    bio = HTMLField()
    role = models.CharField(max_length=200)
    staff_image = models.ImageField(upload_to=upload_staff_img)

    def __unicode__(self):
        return self.user.username
