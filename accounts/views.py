from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.mail import send_mail

# Create your views here.


def signup(request):
    if request.method == 'POST':
        # User has register
        if request.POST['Password'] == request.POST['Password2']:
            try:
                user = User.objects.get(username=request.POST['Username'])
                return render(request, 'account/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['Username'], password=request.POST['Password2'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'account/signup.html', {'error': 'Password must match'})

    else:
        return render(request, 'account/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['Username'], password=request.POST['Password'])
        if user is not None:
            auth.login(request, user)
            send_mail(
                'Subject here',
                'Here is the message.',
                'rishabtest1@yopmail.com',
                ['rishabtest2@yopmail.com'],
                fail_silently=False,
            )
            return redirect('home')
        else:
            return render(request, 'account/login.html', {'error': 'User does not exist'})

    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
