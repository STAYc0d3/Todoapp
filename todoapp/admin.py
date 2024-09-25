from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'deadline']
    list_filter = ['created', 'deadline']
    search_fields = ['title', 'description']
    raw_id_fields = ['author']
    date_hierarchy = 'created'
    show_facets = admin.ShowFacets.ALWAYS