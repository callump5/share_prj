# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *

# Create your views here.

def get_testimonials(request):
    testimonials_list = Testimonial.objects.all()
    return render(request, 'testimonials/testimonials.html', {'list': testimonials_list})
