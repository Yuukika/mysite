from django.contrib import admin
from .models import UserProfile,UserInfo

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone')
    list_filter = ('user', 'birth',)

    ordering = ('user', 'birth',)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'company', 'address', 'aboutme')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
