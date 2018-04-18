# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from contact_us.models import Staff_Contact
# Create your views here.


def get_home(request):
    return render(request, 'home/home.html')