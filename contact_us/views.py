# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.mail import send_mail
from .forms import Contact_Form

from .models import Staff_Contact

from share_prj.settings import EMAIL_HOST_USER, NOTIFY_USER
# Create your views here.

def contact_us(request):

    contacts = Staff_Contact.objects.all()

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
                EMAIL_HOST_USER,
                [NOTIFY_USER]
            )

        messages.success(request, 'Thanks for getting in touch!')

        return redirect('/')

    else:

        contact_form = Contact_Form()

    return render(request, 'contact/contact-form.html', {'form': contact_form,
                                                         'contacts': contacts})



