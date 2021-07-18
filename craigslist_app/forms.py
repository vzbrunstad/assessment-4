from django import forms
from .models import Category, Post

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('item', 'description', 'location') #date field left off of form so user does not have access
