from django.shortcuts import render


def index(req):
    return render(req, 'index.html')


def sign_in(req):
    return render(req, 'sign-in.html')


def sign_up(req):
    return render(req, 'sign-up.html')
