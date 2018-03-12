from django.contrib import admin
from .models import ArticleColumn,ArticlePost

class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ('column',)
    list_filter = ('column',)

    ordering = ('column',)

class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(ArticleColumn, ArticleColumnAdmin)
admin.site.register(ArticlePost, ArticlePostAdmin)