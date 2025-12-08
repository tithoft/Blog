from django import forms

from .models import Blog, Post

class BlogForm(forms.ModelForm):
    """Form for creating new blog."""
    class Meta:
        model = Blog
        fields = ['name']
        labels = {'name': ''}

class PostForm(forms.ModelForm):
    """Form for creating post for a blog."""
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {'body': forms.Textarea(attrs={'cols': 80})}


