from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage
from . forms import UserForm, UserProfileForm
#############################################
def index2(request):

    return render(request, 'basic_app2/index2.html')

def regi(request):
    regis = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            regis = True
        else:
            print (user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, "basic_app2/reg.html",
                  {'user_form':user_form,
                   'profile_form': profile_form,
                   'regis': regis})



#############################################
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
####################################################################

def index1(request):
    context_dict = {'text':'hello world',
                    'number': 100

    }
    return render(request,'basic_app/index1.html', context_dict)


def other(request):
    return render(request,'basic_app/other.html')

def real(request):
    return render(request,'basic_app/realtive_url.html')
