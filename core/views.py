from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(req):
    return render(req, 'index.html')


@login_required(login_url='user signin')
def post_create(req):
    return render(req, 'post-create.html')
