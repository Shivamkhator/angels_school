from django.contrib import admin
from .models import SchoolPage, Gallery

@admin.register(SchoolPage)
class SchoolPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'heading', 'created_at']
    search_fields = ['title', 'heading']
    list_filter = ['created_at']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_added']
    list_filter = ['date_added']
    ordering = ['-date_added']