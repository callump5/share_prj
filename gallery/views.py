# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Staff_Details, Student_Img
# Create your views here.

def get_staff(request):
    staff_list = Staff_Details.objects.all()
    return render(request, 'gallery/staff/list.html', {'staff': staff_list})

def get_students(request):
    students = Student_Img.objects.all()
    return render(request, 'gallery/student/list.html', {'students': students})