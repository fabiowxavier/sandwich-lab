from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import Post, Comment, Like
from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts.
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`blog/index.html`
    """
    queryset = Post.objects.filter(status=1).order_by('title')
    template_name = "blog/index.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for post in context['post_list']:
            # Adding comment and like counts to each post in the context
            post.comment_count = post.comments.filter(approved=True).count()
            post.like_count = post.likes.count()
        return context


def post_list(request):
    """
    List all published posts on the home page.
    """
    queryset = Post.objects.filter(status=1)
    return render(request, "blog/index.html", {
        "post_list": queryset,
    })


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    # Handle like functionality
    if request.method == "POST" and request.user.is_authenticated:
        if 'like' in request.POST:
            # Check if the user has already liked this post
            existing_like = Like.objects.filter(post=post, user=request.user)
            if existing_like.exists():
                existing_like.delete()  # Unlike the post
                messages.info(request, "You unliked this post.")
            else:
                # Like the post
                Like.objects.create(post=post, user=request.user)
                messages.success(request, "You liked this post.")

    like_count = post.likes.count()  # Count the likes on the post

    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            if comment_form.instance.pk:
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                messages.success(request, "Comment updated successfully!")
            else:  
                comment = comment_form.save(commit=False)
                comment.post = post
                if request.user.is_authenticated:
                    comment.author = request.user
                    comment.name = request.user.username
                else:
                    comment.name = "Anonymous"
                comment.save()
                messages.success(request, "Comment submitted and awaiting approval.")

    else:
        comment_form = CommentForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "like_count": like_count,  # Pass the like count to the template
        "comment_form": comment_form,
    })



def comment_edit(request, comment_id):
    # Retrieve the comment object by its ID
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Check if the request method is POST
    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            # Save the updated comment
            comment_form.save()
            messages.success(request, "Comment updated successfully!")
            # Redirect to the post detail page after update
            return redirect('post_detail', slug=comment.post.slug)  # Redirect to the post detail page
    else:
        comment_form = CommentForm(instance=comment)
    
    return render(request, 'blog/post_detail.html', {'comment_form': comment_form, 'comment': comment})


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Comment deleted!")
    else:
        messages.error(request, "You can only delete your own comments!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))
