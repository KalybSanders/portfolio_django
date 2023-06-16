from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Contact

def home(request):
    contact = Contact.objects.all()
    return render(request, 'home.html', {'contact': contact})

def contact(request):
    if request.method == 'POST':
        fullName = request.POST['fullName']
        phoneNumber = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        new_contact = Contact.objects.create(
            fullName=fullName, phoneNumber=phoneNumber, email=email, message=message
        )
        new_contact.save()

        return redirect('home')
    else:
        return render(request, "home.html")
