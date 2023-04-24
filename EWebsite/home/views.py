from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

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
    
def features(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'features.html')

def pricing(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'pricing.html')

def faq(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'faq.html')

def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'about.html')

def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'contact.html')
