from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.forms import PostForm
from core.models import Post

# def handler404(request, exception):
#     return render(request, '404.html', status=404)


def index(req):
    current_user = req.user
    first_post = Post.objects.first()
    page = "home-page"
    posts = Post.objects.order_by('-id')[:4]
    context = {
        'current_user': current_user, 'posts': posts, 'first_post': first_post, "page": page,
    }
    return render(req, 'index.html', context)


@login_required(login_url='user signin')
def post_create(req):
    page = "post-create-page"
    if req.method == 'GET':
        context = {
            'current_user': req.user,
            'form': PostForm(),
            'page': page,
        }
        return render(req, 'post-create.html', context)
    creator_obj = req.user.userprofile
    creator_post = Post(creator=creator_obj)
    form = PostForm(req.POST, req.FILES, instance=creator_post)
    if form.is_valid():
        form.save()
        return redirect('post list')
    context = {
        'form': form,
        'current_user': req.user,
        'page': page,
    }
    return render(req, 'post-create.html', context)


@login_required(login_url='user signin')
def post_details(req, pk):
    page = "post-details-page"
    current_user = req.user
    post = Post.objects.get(pk=pk)
    tags = post.tags.split(", ")
    tags = [tag.upper() for tag in tags]
    context = {
        'post': post,
        'tags': tags,
        'has_permissions': current_user.userprofile == post.creator,
        'current_user': current_user,
        'page': page,
    }
    return render(req, 'post-details.html', context)


@login_required(login_url='user signin')
def post_edit(request, pk):
    page = "post-edit-page"
    current_user = request.user
    post = Post.objects.get(pk=pk)
    if current_user.userprofile != post.creator:
        context = {
            'current_user': current_user,
            'page': page,
        }
        return render(request, 'access-denied.html', context)
    if request.method == 'GET':
        post_form = PostForm(instance=post)
        context = {
            'post': post, 'post_form': post_form, 'current_user': current_user, 'page': page,
        }
        return render(request, 'post-edit.html', context)
    post_form = PostForm(request.POST, request.FILES, instance=post)
    if post_form.is_valid():
        post_form.save()
        return redirect('post details', post.pk)
    context = {
        'post_form': post_form,
        'current_user': current_user,
        'page': page,
    }
    return render(request, 'post-edit.html', context)


@login_required(login_url='user signin')
def post_list(request):
    page = "post-list-page"
    current_user = request.user
    if request.method == 'GET':
        posts = Post.objects.order_by('-id')
        context = {
            'current_user': current_user,
            'posts': posts,
            'page': page,
        }
        return render(request, 'post-list.html', context)
    search_result = request.POST.get('search-field').lower()
    posts = Post.objects.order_by('-id')
    posts = [post for post in posts if search_result in post.title.lower() or search_result in post.tags.lower()]
    context = {
        'current_user': current_user,
        'posts': posts,
        'page': page,
    }
    return render(request, 'post-list.html', context)


@login_required(login_url='user signin')
def post_delete(request, pk):
    page = "post-delete-page"
    current_user = request.user
    post = Post.objects.get(pk=pk)
    if current_user.userprofile != post.creator:
        context = {
            'current_user': current_user,
            'page': page,
        }
        return render(request, 'access-denied.html', context)
    if request.method == 'GET':
        context = {
            'post': post, 'current_user': current_user, 'page': page,
        }
        return render(request, 'post-delete.html', context)
    post.delete()
    return redirect('post list')
