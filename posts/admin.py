from django.contrib import admin
from .models import Post, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'content', 'created_at', 'updated_at']
    list_filter = ['category']
    search_fields = ['title', 'content']
    list_editable = ['author']
    
    
admin.site.register(Category)
admin.site.register(Tag)
