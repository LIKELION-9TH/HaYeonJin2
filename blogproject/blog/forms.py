from django import forms
from .models import Blog, Pastime, Place, Music, Photo
from ckeditor_uploader.widgets import CKEditorUploadingWidget
 
class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog

        fields = ['title', 'author', 'content'] 

        
 
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 600px', 'placeholder': '제목을 입력하세요.'}
            ),
            'author': forms.Select(
                attrs={'class': 'custom-select'},
            ),
            'content': forms.CharField(widget=CKEditorUploadingWidget()),
        }


class CreatePastime(forms.ModelForm):
    class Meta:
        model = Pastime

        fields = ['title', 'author', 'content'] 
 
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 600px', 'placeholder': '제목을 입력하세요.'}
            ),
            'author': forms.Select(
                attrs={'class': 'custom-select'},
            ),
            'content': forms.CharField(widget=CKEditorUploadingWidget()),
        }

class CreatePlace(forms.ModelForm):
    class Meta:
        model = Place

        fields = ['title', 'author', 'content'] 
 
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 600px', 'placeholder': '제목을 입력하세요.'}
            ),
            'author': forms.Select(
                attrs={'class': 'custom-select'},
            ),
            'content': forms.CharField(widget=CKEditorUploadingWidget()),
        }


class CreateMusic(forms.ModelForm):
    class Meta:
        model = Music

        fields = ['title', 'author', 'content'] 
 
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 600px', 'placeholder': '제목을 입력하세요.'}
            ),
            'author': forms.Select(
                attrs={'class': 'custom-select'},
            ),
            'content': forms.CharField(widget=CKEditorUploadingWidget()),
        }


class FaceForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
        'title',
        'image',
        'description'
        ]