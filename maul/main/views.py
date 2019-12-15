from django.shortcuts import render
from django.http import HttpResponse
from .models import Services
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"services": Services.objects.all})


def register(request):
    form = UserCreationForm
    return render(request=request,
                  template_name="main/register.html",
                  context={"form": form})