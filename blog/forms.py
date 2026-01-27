from .models import Comment
from django import forms

# forms.ModelForm is a built-in Django class.
# As a result, we can use the Meta class to tell
# he ModelForm class what models and fields we want in our form. 
# form.ModelForm will then build this for us.

# We included the body field for the user to complete.
# This field was imported from the Comment model.
# We didn't need to include the other fields because the post,
# user and created_on fields in our model are filled in automatically,
# and the approved field is managed by the superuser.

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
