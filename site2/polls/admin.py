from django.contrib import admin

from .models import Post, Page

# admin.site.register(Post)
# admin.site.register(Page)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'author']
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
	list_display = ['ptitle']