# forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image', 'video']

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

class LikeForm(forms.Form):
    pass
