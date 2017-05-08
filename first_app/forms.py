from django import forms
from django.core import validators

#these below methods can be used for singl field "from django.core import validators"
def check_for_n(value):
    if value[0] != "z":
        raise validators.ValidationError("start with Z")
def check_for_t(value):
    if len(value) < 10:
        raise validators.ValidationError("please eneter more then 10 charechrot")



class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_n])
    email = forms.EmailField()
    veri_email = forms.EmailField(label="Enter email again ")
    text = forms.CharField(widget=forms.Textarea, validators=[check_for_t])
    bot = forms.CharField(required=False, widget=forms.HiddenInput,
                         validators=[validators.MaxLengthValidator(0)])

    #to clean the entire form, we can use below mthods
    def clean(self):
        all_clean_data = super().clean() #this will grap all the clean data at once
        email = all_clean_data['email']
        vmail = all_clean_data['veri_email']

        if email != vmail:
            raise forms.ValidationError("Make sure email match")

