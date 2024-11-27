from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    context_object_name = 'post_list'
    paginate_by = 9
    
    def index(request): 
        context = { 'title': 'Welcome to the Blog', 'posts': Post.objects.all() # Assuming you have a Post model 
        }
        return render(request, 'blog/index.html', context)