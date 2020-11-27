from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from accounts.forms import SignupForm
from accounts.models import UserProfile


def signup_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        context = {
            'form': SignupForm(),
        }
        return render(request, 'sign-up.html', context)
    form = SignupForm(request.POST)
    if form.is_valid():
        user = form.save()
        profile = UserProfile(
            user=user,
        )
        profile.save()
        login(request, user)
        return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'sign-up.html', context)


def signin_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect.')
    return render(request, 'sign-in.html')

def signout_user(request):
    logout(request)
    return redirect('home')