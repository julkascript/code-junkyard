from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
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


@login_required(login_url='user signin')
def signout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='user signin')
def user_profile(request, pk):
    current_user = request.user
    user_obj = User.objects.get(pk=pk)
    context = {
        'user': user_obj,
        'current_user': current_user,
        'profile': user_obj.userprofile,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='user signin')
def user_profile_edit(request, pk):
    user_obj = User.objects.get(pk=pk)
    current_user = request.user
    if user_obj != current_user:
        context = {
            'current_user': current_user,
        }
        return render(request, 'access-denied.html', context)
    if request.method == 'GET':
        form = UserProfileForm(instance=user_obj.userprofile)
        context = {
            'form': form,
            'current_user': user_obj,
            'user': user_obj,
        }
        return render(request, 'profile-edit.html', context)
    # old_img = user_obj.userprofile.profile_picture
    form = UserProfileForm(request.POST, request.FILES, instance=user_obj.userprofile)
    if form.is_valid():
        # if old_img:
        #     clean_up_files(old_img.path)
        form.save()
        return redirect('user profile', user_obj.pk)
    context = {
        'form': form,
        'user': user_obj,
        'current_user': user_obj,
    }
    return render(request, 'profile.html', context)
