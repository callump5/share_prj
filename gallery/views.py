# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Staff_Details
# Create your views here.

def get_staff(request):
    staff_list = Staff_Details.objects.all().order_by('role').reverse()
    return render(request, 'gallery/staff/list.html', {'staff': staff_list})
