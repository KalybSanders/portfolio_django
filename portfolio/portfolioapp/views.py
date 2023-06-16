from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Contact

def home(request):
    return render(request, 'home.html')

def contact(request):
    # do stuff
    return

