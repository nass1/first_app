from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage
from . import forms

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_recored':webpages_list }


    return render(request, 'index.html', context = date_dict)


def form_name(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            print ("Post is working")
            print (form.cleaned_data["name"])
            print ("thi is text " + form.cleaned_data["text"])




    return render(request, "form_page.html", {'form':form})
