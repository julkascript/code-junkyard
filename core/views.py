from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.forms import PostForm
from core.models import Post


def index(req):
    return render(req, 'index.html')


@login_required(login_url='user signin')
def post_create(req):
    if req.method == 'GET':
        context = {
            'form': PostForm()
        }
        return render(req, 'post-create.html', context)
    creator_obj = req.user.userprofile
    creator_post = Post(creator=creator_obj)
    form = PostForm(req.POST, req.FILES, instance=creator_post)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {'form': form}
    return render(req, 'post-create.html', context)

