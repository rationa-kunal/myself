from django import forms

from .models import BlogPost

class newBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'intro', 'post', 'img_url',)
