from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'category',
            'tags',
            'content',
            'status'
        ]

        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }
