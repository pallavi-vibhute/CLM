from django import forms
from models import *

class ContactForm(forms.Form):
    full_name = forms.CharField()
    phone = forms.IntegerField()
    email = forms.EmailField()
    
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'phone', 'email']
        