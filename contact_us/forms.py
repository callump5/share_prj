from django.forms import ModelForm

from .models import *

class Contact_Form(ModelForm):

    class Meta:
        model = Contact_Info
        fields = ['name', 'number', 'email', 'text']
