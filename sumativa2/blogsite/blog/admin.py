from django.contrib import admin
from .models import post, Category, Hashtag, Entry

# Register your models here.
admin.site.register(post)
admin.site.register(Category)
admin.site.register(Hashtag)
admin.site.register(Entry)