from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Post

class PostView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post




# Create your views here.
