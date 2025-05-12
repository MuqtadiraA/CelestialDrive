from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    return render(request, "products/index.html")

def about(request):
    return render(request, "products/about.html")

def contact(request):
    return render(request, "products/contact.html")

def signin(request):
    return render(request, "products/signin.html")

#Cars: 
def car1(request):
    return render(request, 'products/car1.html')

def car2(request):
    return render(request, 'products/car2.html')

def car3(request):
    return render(request, 'products/car3.html')

def car4(request):
    return render(request, 'products/car4.html')

def car5(request):
    return render(request, 'products/car5.html')

def car6(request):
    return render(request, 'products/car6.html')

def car7(request):
    return render(request, 'products/car7.html')

def car8(request):
    return render(request, 'products/car8.html')

def car9(request):
    return render(request, 'products/car9.html')

def car10(request):
    return render(request, 'products/car10.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'products/contact.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('signin')  # Adjust if your login page is named differently

    return render(request, 'products/signup.html')