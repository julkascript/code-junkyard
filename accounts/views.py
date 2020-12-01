from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import SignupForm, UserProfileForm
from accounts.models import UserProfile
from core.clean_up import clean_up_files


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


def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user,
        'profile': user.userprofile,
    }
    return render(request, 'profile.html', context)


def user_profile_edit(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'GET':
        form = UserProfileForm(instance=user.userprofile)
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'profile-edit.html', context)
    old_img = user.userprofile.profile_picture
    form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
    if form.is_valid():
        if old_img:
            clean_up_files(old_img.path)
        form.save()
        return redirect('user profile', user.pk)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'profile.html', context)
