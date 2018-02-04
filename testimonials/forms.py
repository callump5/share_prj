from django import forms
from tinymce.widgets import TinyMCE
from models import *

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimonial