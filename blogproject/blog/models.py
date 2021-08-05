from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)
    content = RichTextUploadingField(null=True)

class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length=500)


class Pastime(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)
    content = RichTextUploadingField(null=True)

class Place(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)
    content = RichTextUploadingField(null=True)

class Music(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)
    content = RichTextUploadingField(null=True)
