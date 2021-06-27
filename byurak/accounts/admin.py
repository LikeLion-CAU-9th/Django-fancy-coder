from django.contrib import admin
from accounts.models import User, Profile, UserFollow


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'nickname']
    list_display_links = ['email', 'nickname']
    
admin.site.register(Profile)
admin.site.register(UserFollow)

