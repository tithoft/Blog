from django.shortcuts import render, redirect

from .models import Blog, Post
from .forms import BlogForm, PostForm

def index(request):
    """The home page for the Blog."""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Page to view all blogs."""
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """Page to view selected blog and its posts."""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.post_set.order_by('-date_added')
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)

def new_blog(request):
    """Add a new blog."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
        
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

def new_post(request, blog_id):
    """Add a new post for a blog."""
    blog = Blog.objects.get(id=blog_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blog', blog_id=blog_id)
        
    # Display a blank or invalid form.
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    """Edit existing post."""
    post = Post.objects.get(id=post_id)
    blog = post.blog

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)
        
    context = {'post': post, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
