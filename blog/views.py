from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
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
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")  # Fetch all comments ordered by creation
    comment_count = post.comments.filter(approved=True).count()

    # Handle comment submission and editing
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # Check if it's an update
            if comment_form.instance.pk:  # If the form has a primary key, it's an update
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                messages.success(request, "Comment updated successfully!")
            else:  # It's a new comment
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
        "comment_form": comment_form,
    })

def comment_edit(request, slug, comment_id):
    """
    Edit a comment.
    """
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()  # Save the edited comment
            messages.success(request, "Comment updated successfully!")
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))  # Redirect back to the post detail page
        else:
            messages.error(request, "There was an error updating your comment.")

    # If it's a GET request, show the edit form
    comment_form = CommentForm(instance=comment)

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": post.comments.all().order_by("-created_on"),
        "comment_form": comment_form,
    })


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.
    """
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:  # Ensure only the author can delete their comment
        comment.delete()
        messages.success(request, "Comment deleted!")
    else:
        messages.error(request, "You can only delete your own comments!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))