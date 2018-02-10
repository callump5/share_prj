# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages

from django.core.mail import send_mail
from .forms import Contact_Form

# Create your views here.

def contact_us(request):

    if request.method == 'POST':

        contact_form = Contact_Form(request.POST)

        if contact_form.is_valid():
            contact = contact_form.save()
            contact.save()


            message = "Name:" + contact.name + "\n" +\
                      "Number:" + contact.number + "\n" +\
                      "Email:" + contact.email + "\n" +\
                      "Text:" + contact.text


            send_mail(
                'Contact Request',
                message,
                'clpullinger@gmail.com',
                ['']
            )

        messages.success(request, 'Thanks for getting in touch!')

        return render(request, 'home/home.html')

    else:

        contact_form = Contact_Form()

    return render(request, 'contact/contact-form.html', {'form': contact_form})



