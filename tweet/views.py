from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'tweet/index.html'

# Create your views here.
