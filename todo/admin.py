from django.contrib import admin

from .models import Project, Issue

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['title', 'description', 'created_at', 'updated_at']
    search_fields=['title']

admin.site.register(Issue)