# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from contact_us.models import Staff_Contact
from .models import SlideImage, LandingBox, LandingContent
# Create your views here.


def get_home(request):
    slides = SlideImage.objects.all()
    landing = LandingContent.objects.all()
    boxes = LandingBox.objects.all()
    return render(request, 'home/home.html', {'slides': slides, 'landing': landing, 'boxes': boxes})
