from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # '<slug:slug>/' = first slug defines data type as a slug, the second
    # slug after the colon returns the post.slug into the URL path.
    # Another example would be '<str:name>/' to define data type as a
    # string, then the name value to the URL path.
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
