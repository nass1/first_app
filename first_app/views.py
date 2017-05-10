from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import AccessRecord, Topic, Webpage
from . forms import UserForm, UserProfileForm


##################################################### start of log in Log out
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index2'))



@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")



def user_login(request):
    print ("test 123")
    print (request.POST.get('username'))
    print (request.POST.get('password'))

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                print ("after this we check if user active")
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                print ("index2 if")
                return HttpResponseRedirect(reverse('index2'))
            else:
                # If account is not active:
                print ("index2 else")
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        print ("last else")
        return render(request, 'basic_app2/login.html', {})





















############################################# start of log in Log out
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
