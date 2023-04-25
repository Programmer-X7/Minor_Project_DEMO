from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from home.models import Contact


# Create your views here.

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'about.html')

def pricing(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'pricing.html')

def faq(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'faq.html')


def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('emaildesc')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()

    return render(request, 'contact.html')
