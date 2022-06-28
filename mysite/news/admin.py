from django.contrib import admin
from .models import News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created', 'updated', 'photo']
    list_display_links = ['title', 'content']
    search_fields = ['title', 'content']

admin.site.register(News, NewsAdmin)