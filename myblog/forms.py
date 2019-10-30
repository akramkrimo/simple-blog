from django import forms
from .models import Blog

class CreateBlog(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    thumbnail = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'input-group-text ',
            }
        ),label=''
    )

class AddComment(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )
