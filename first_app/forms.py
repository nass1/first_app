from django import forms
from django.core import validators

def check_for_n(value):
    if value[0] != "z":
        raise validators.ValidationError("start with Z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_n])
    email = forms.EmailField()
    veri_email = forms.EmailField(label="Enter email again ")
    text = forms.CharField(widget=forms.Textarea)
    bot = forms.CharField(required=False, widget=forms.HiddenInput,
                         validators=[validators.MaxLengthValidator(0)])

