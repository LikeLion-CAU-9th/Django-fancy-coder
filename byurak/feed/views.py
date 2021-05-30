from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import *


def service_landing(request):
    return render(request, 'landing.html')


def post_home(request):
    return render(request, template_name="post_home.html")


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.host = request.user
            post.image = request.FILES.get('image')
            post.save()
            return redirect('post:post_detail', post.pk)
    else:
        form = PostForm()
        context = {
            'form':form,
        }
        return render(request, "post_create.html", {"form": form})


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, "post_list.html", context=context)


def post_detail(request, pk):
    #post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post':post,
    }
    return render(request, "post_detail.html", context=context)


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = postForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.image = request.FILES.get('image')
            post.save()
            return redirect('post:post_detail', pk)
    else:
        form = PostForm(instance=post)
        context = {
            'form': form,
            'pk': pk,
        }
    return render(request, 'post_update.html', context=context)


def post_delete(request, pk):

    if request.method=="GET":
        context = {
            'pk':pk
        }
        return render(request, "post_delete.html", context=context)
        
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post:post_home')