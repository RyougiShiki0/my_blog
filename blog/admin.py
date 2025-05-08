from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Category)