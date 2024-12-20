from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))
"""
Stores a single blog post entry related to :model:`auth.User`.
"""
class Post(models.Model): 
    title = models.CharField(max_length=200, unique=True) 
    slug = models.SlugField(max_length=200, unique=True) 
    author = models.ForeignKey( User, on_delete=models.CASCADE, related_name="blog_posts" ) 
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField(default="Default content") 
    created_on = models.DateTimeField(auto_now_add=True) 
    status = models.IntegerField(choices=STATUS, default=0) 
    excerpt = models.TextField(blank=True) 
    updated_on = models.DateTimeField(auto_now=True) 
    location = models.CharField(max_length=100, default="Unknown")
    
    
    class Meta: 
        ordering = ["-created_on"] 
            
    def __str__(self): 
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80, default="Anonymous")
    email = models.EmailField(default="default@example.com")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
    

class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Like from {self.user} on {self.post}"