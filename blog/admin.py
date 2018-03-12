from django.contrib import admin
from .models import BlogArticles

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    list_filter = ('title', 'publish')

    ordering = ('title', 'publish')

admin.site.register(BlogArticles, BlogArticlesAdmin)