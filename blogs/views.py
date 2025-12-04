from django.shortcuts import render, redirect

from .models import Blog

def index(request):
    """The home page for the Blog."""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Page to view all blogs."""
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)
