from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .backends import EmailBackend

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('login successful')
        else:
            return render(request, 'account/signin.html', {"error": "Invalid credentials"})
    return render(request, 'account/signin.html')