# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.mail import send_mail
from .forms import Contact_Form

from .models import Staff_Contact

from .send_email import my_send_mail
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

            subject = "Contact Request"

            my_send_mail(contact.name, contact.email, contact.number, contact.text)

        messages.success(request, 'Thanks for getting in touch!')

        return redirect('/')

    else:

        contact_form = Contact_Form()

    return render(request, 'contact/contact-form.html', {'form': contact_form,
                                                         'contacts': contacts})



