from audioop import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Post

class PostListView(CreateView):
    model = Post

class PostCreatView(CreateView):
    model = Post
    fields = "--all--"
    success_url: reverse_lazy("blog:all")

class PostDetailView(CreateView):
    model = Post


class PostUpdateView(CreateView):
    model = Post
    fields = "--all--"
    success_url: reverse_lazy("blog:all")

class PostDeleteView(CreateView):
    model = Post
    fields = "--all--"
    success_url: reverse_lazy("blog:all")