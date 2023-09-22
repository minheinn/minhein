from django import forms
from . models import *

class AboutForm(forms.ModelForm):
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
            'image':forms.FileInput(attrs=({"placeholder":"Image", "id":"image", "onchange":"getImagePreview(event)"})),
        }

class TypeWriterForm(forms.ModelForm):
    class Meta:
        model = TypeWriter
        fields = "__all__"
        widgets = {
            'text':forms.TextInput(attrs=({'placeholder':'Write one Text..'})),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        widgets = {
            'skill':forms.TextInput(attrs=({'placeholder':'Write Your Skill..'})),
            'percent':forms.NumberInput(attrs=({'placeholder':"Write Your Skill Percents.."})),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        widgets = {
            'title':forms.TextInput(attrs=({'placeholder':'Write Title'})),
            'image':forms.FileInput(attrs=({"placeholder":"Image", "id":"image", "onchange":"getImagePreview(event)"})),
            'description':forms.Textarea(attrs=({'placeholder':'Write Description'})),
        }