from django.forms import form

from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'draft']