from django.contrib import admin

# The dot in front of models below indicates that we are importing Post 
# from a file named models, which is in the same directory as
# our admin.py file. 
# If you have multiple models that you want to import, 
# then you can separate them with a comma. 
# For example, in future topics, you will create a Comment model, 
# which will need to be imported at that point.

from .models import Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
