from django.db import models

class Blog(models.Model):
    """A user's blog."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
    
class Post(models.Model):
    """Individual post in blog."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return sring representation of the post."""
        if len(self.title) > 50:
            return f"{self.title[:50]}..."
        else:
            return self.title
    