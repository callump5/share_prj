# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

import dropbox
from share_prj.settings import dbx
# Create your models here.

class Staff_Details(models.Model):
    user = models.ForeignKey(User, related_name='staff_profile')
    bio = HTMLField()
    staff_image = models.ImageField(upload_to='images', blank=True, null=True)

    def __unicode__(self):
        return self.user.username
