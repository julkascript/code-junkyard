from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.forms import PostForm
from core.models import Post


def index(req):
    current_user = req.user
    context = {'current_user': current_user}
    return render(req, 'index.html', context)


@login_required(login_url='user signin')
def post_create(req):
    if req.method == 'GET':
        context = {
            'current_user': req.user,
            'form': PostForm()
        }
        return render(req, 'post-create.html', context)
    creator_obj = req.user.userprofile
    creator_post = Post(creator=creator_obj)
    form = PostForm(req.POST, req.FILES, instance=creator_post)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {'form': form, 'current_user': req.user}
    return render(req, 'post-create.html', context)


@login_required(login_url='user signin')
def post_details(req, pk):
    current_user = req.user
    post = Post.objects.get(pk=pk)
    tags = post.tags.split(", ")
    context = {
        'post': post, 'tags': tags, 'has_permissions': current_user == post.creator, 'current_user': current_user
    }
    return render(req, 'post-details.html', context)


@login_required(login_url='user signin')
def post_edit(request, pk):
    current_user = request.user
    post = Post.objects.get(pk=pk)
    if current_user.userprofile != post.creator:
        context = {'current_user': current_user}
        return render(request, 'access-denied.html', context)
    if request.method == 'GET':
        post_form = PostForm(instance=post)
        context = {
            'post': post, 'post_form': post_form, 'current_user': current_user
        }
        return render(request, 'post-edit.html', context)
    post_form = PostForm(request.POST, request.FILES, instance=post)
    if post_form.is_valid():
        post_form.save()
        return redirect('post details', post.pk)
    context = {
        'post_form': post_form,
        'current_user': current_user,
    }
    return render(request, 'post-edit.html', context)
