from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


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

    # Python functions always have a return. The path to
    # the template file is included in the view function return.
    # render() is a shortcut to load data to a template and return it.

    # The response our view is returning is the contents of a webpage
    # containing one post. In this view, we pass the request object,
    # the path to the template and a dictionary of data to the
    # Django render() helper function.
    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )
