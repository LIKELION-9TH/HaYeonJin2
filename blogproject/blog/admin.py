from django.contrib import admin
from .models import Blog, Pastime, Place, Music
from .models import Photo
# Register your models here.

admin.site.register(Blog)
admin.site.register(Photo)
admin.site.register(Pastime)
admin.site.register(Place)
admin.site.register(Music)