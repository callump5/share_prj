# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .send_email import my_send_mail, authError
from smtplib import SMTPAuthenticationError

from .forms import Contact_Form

from .models import Staff_Contact
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

            my_send_mail(request, contact.name, contact.email, contact.number, contact.text)


        return redirect('/')

    else:

        contact_form = Contact_Form()

    return render(request, 'contact/contact-form.html', {'form': contact_form,
                                                         'contacts': contacts})



