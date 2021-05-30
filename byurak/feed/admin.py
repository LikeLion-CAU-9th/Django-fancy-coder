from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "body", "date_time"]
    list_display_links = ["title", "body", "date_time"]