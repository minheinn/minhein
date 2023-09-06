from django import forms
from . models import About

class aboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = "__all__"
        widgets = {
            'name':forms.TextInput(attrs=({'placeholder':'Enter Your Name..'})),
            'birthday':forms.DateInput(attrs=({'type':'date'})),
            'email':forms.EmailInput(attrs=({'placeholder':'Enter Your Email..'})),
            'phone':forms.TextInput(attrs=({'placeholder':'Enter Your Phone..'})),
            'address':forms.TextInput(attrs=({'placeholder':'Enter Your Address..'})),
            'description':forms.Textarea(attrs=({'placeholder':'Enter Your Description..'})),
        }