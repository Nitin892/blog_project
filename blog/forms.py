from django import forms
from .models import Post,Comment
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)



class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
