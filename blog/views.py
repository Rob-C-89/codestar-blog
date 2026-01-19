from django.shortcuts import render
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
    template_name = "post_list.html"