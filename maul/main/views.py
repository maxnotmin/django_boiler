from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Services
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"services": Services.objects.all})



def about(request):
    return render(request=request,
                  template_name="main/about.html",
                  context={"services": Services.objects.all})


def silencearlert(request):
    return render(request=request,
                  template_name="main/silencealert.html",
                  context={"services": Services.objects.all})

def createarlert(request):
    return render(request=request,
                  template_name="main/createalert.html",
                  context={"services": Services.objects.all})

def automation(request):
    return render(request=request,
                  template_name="main/automation.html",
                  context={"services": Services.objects.all})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "New Account Created: {user}".format(user=username))
            login(request, user)
            messages.info(request, "You are now logged in as: {user}".format(user=username))
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print("Error :", str(form.error_messages[msg]))
                messages.error(request, "{mes} : {formerror}".format(mes=msg, formerror=str(form.error_messages[msg])))
    form = UserCreationForm
    return render(request,
                  template_name="main/register.html",
                  context={"form": form})

