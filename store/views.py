from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models import *
from store.models import user1

def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from .models import user1

def index(request):
    return render(request, 'index.html')

def signup(request):
    if 'email' in request.GET and 'password' in request.GET:
        u = user1()
        u.email = request.GET['email']
        u.password = request.GET['password']
        u.save()
        print("User saved:", u.email)  # Debugging line

    return redirect('/index')  # Redirect to index.html after saving

def login(request):
    email = request.GET.get('email')  
    password = request.GET.get('password')

    if user1.objects.filter(email=email, password=password).exists():
        request.session['logged_in'] = True  # Set session variable
        return render(request, 'index.html')  
    else:
        return HttpResponse("<script>alert('Invalid email or password'); window.location='/index';</script>")

def logout(request):
    request.session.flush()  # Clear all session data
    return redirect('/index')  # Redirect to index

