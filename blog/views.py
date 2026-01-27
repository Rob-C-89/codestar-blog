from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.
class PostList(generic.ListView):
    # model = Post

    # Filter by author ID
    # queryset = Post.objects.filter(author=4)

    # Display in order of time created (add "-" to reverse)
    # queryset = Post.objects.all().order_by("created_on")

    # Filter by Published status, i.e. filter out Drafts
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

# A view function takes a web request and returns a web response.
# A function-based view always passes in the request object as the
# first argument to the view. Convention dictates that we call this
# parameter request, but in fact, we could call it anything we want.

# In addition, we have passed in the slug parameter, which
# gets the argument value from the URL pattern named post_detail.


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    # status=1 is filterign objects which have the published status
    # we can use the shortcut get_object_or_404() to get data or
    # raise a Http404 error if the data object does not exist.
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    # Python functions always have a return. The path to
    # the template file is included in the view function return.
    # render() is a shortcut to load data to a template and return it.

    # The response our view is returning is the contents of a webpage
    # containing one post. In this view, we pass the request object,
    # the path to the template and a dictionary of data to the
    # Django render() helper function.

    # The object is being passed to the template as a
    # Python dictionary, {"post": post}. We retrieve one single
    # blog post, store it in a variable called post and pass that
    # through to the template in a dictionary where both the value and
    # key name are post. This is called context and it is how you pass
    # data from your own views to a template.
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
