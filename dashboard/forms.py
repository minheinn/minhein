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
        
## For Facts
class FactForm(forms.ModelForm):
    class Meta:
        model = Fact
        fields = "__all__"
        widgets = {
            'fact':forms.TextInput(attrs=({'placeholder':'Write one Fact..'})),
            'number':forms.NumberInput(attrs=({'placeholder':'Choose one number'})),
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

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"
        widgets = {
            'subject':forms.Select(attrs=({'class':'custom_input'})),
            'image':forms.FileInput(attrs=({"placeholder":"Image", "id":"image", "onchange":"getImagePreview(event)"})),
        }