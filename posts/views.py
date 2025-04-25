from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post, Item  # Ensure both Post and Item models exist
from .forms import PostForm2  # Import PostForm2
from .serializers import PostSerializer
import random


def test_view(request):
    return HttpResponse(f"Hello world {random.randint(1, 100)}")


def html_view(request):
    return render(request, "base.html")


def item_list_view(request):
    items = Item.objects.all()  # Ensure Item is defined in models.py
    return render(request, "items/item_list.html", {"items": items})


@login_required(login_url="/users/login/")
def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "posts/post_list.html", context={"posts": posts})


@login_required(login_url="/users/login/")
def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "posts/post_detail.html", {"post": post})


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@login_required(login_url="/login/")
def post_update_view(request, post_id):
    post = Post.objects.filter(id=post_id, author=request.user).first()
    if not post:
        return HttpResponseForbidden("403 Forbidden")

    if request.method == "GET":
        form = PostForm2(instance=post)
        return render(request, "posts/post_update.html", context={"form": form})

    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request, "posts/post_update.html", context={"form": form})

        tags = form.cleaned_data.pop("tags", None)  # Safely handle missing tags
        form.save()
        if tags:
            post.tags.set(tags)  # Ensure tags are updated only if provided
        return redirect("/posts/")