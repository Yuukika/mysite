from django.contrib import admin
from .models import ArticleColumn,ArticlePost,Articletag

class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ('column',)
    list_filter = ('column',)

    ordering = ('column',)

class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
admin.site.register(ArticleColumn, ArticleColumnAdmin)
admin.site.register(ArticlePost, ArticlePostAdmin)
admin.site.register(Articletag, ArticleTagAdmin)