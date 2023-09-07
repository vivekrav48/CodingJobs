from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  login

from job.models import Job
from userprofile.models import Userprofile

# Create your views here.

def homepage(request):
    jobs = Job.objects.all()[0:3]
    return render(request, "homepage.html", {'jobs':jobs})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'jobseeker')

            if account_type == 'employer':
                userprofile = userprofile.objects.create(user=user, is_employer=True)
                # user.userprofile.is_employer = True
                userprofile.save()
            else:
                userprofile = userprofile.objects.create(user=user)
                # user.userprofile.is_employer = True
                userprofile.save()

            login(request,user)

            return redirect("homepage")
    
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {'form': form})

