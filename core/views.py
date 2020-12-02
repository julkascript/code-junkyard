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


@login_required(login_url='user signin')
def post_details(req, pk):
    user = req.user
    post = Post.objects.get(pk=pk)
    tags = post.tags.split(", ")
    context = {
        'user': user, 'post': post, 'tags': tags, 'has_permissions': user == post.creator
    }
    return render(req, 'post-details.html', context)


@login_required(login_url='user signin')
def post_edit(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    if user != post.creator:
        return render(request, 'access-denied.html')
    if request.method == 'GET':
        post_form = PostForm(instance=post)
        context = {
            'user': user, 'post': post, 'post_form': post_form
        }
        return render(request, 'post-edit.html', context)
    post_form = PostForm(request.POST, request.FILES, instance=post)
    if post_form.is_valid():
        post_form.save()
        return redirect('post details', post.pk)
    context = {
        'post_form': post_form,
    }
    return render(request, 'post-edit.html', context)
