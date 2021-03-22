from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ("board", "status", "title", "author", "created_on", "display_date")
    list_display_links = ("board", "status", "title", "author", "created_on")
    list_filter = ("board", "status", "author", "created_on")
