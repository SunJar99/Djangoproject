from django.shortcuts import render, HttpResponse
import random
from posts.models import Post
from .serializers import PostSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.contrib.auth.decorators import login_required
from .models import Items

def test_view(request):
    return HttpResponse(f"Hello world {random.randint(1, 100)}")


def html_view(request):
    return render(request, "base.html")

def item_list_view(request):
    items = Item.objects.all()
    return render(request, "items/item_list.html", {"items": items})

@login_required(login_url="/users/login/")
def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "posts/post_list.html", context={"posts": posts})

@login_required(login_url="/users/login/")
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/post_detail.html", {"post": post})

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer