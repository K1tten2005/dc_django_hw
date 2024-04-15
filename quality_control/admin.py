from django.contrib import admin
from .models import BugReport, FeatureRequest


# Класс администратора для модели Project
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'priority', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    fieldsets = [
        (
            None,
            {
                'fields': ('title', 'description', 'project', 'task', 'status', 'priority')
            }
        )
    ]


# Класс администратора для модели Task
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'priority', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = [
        (
            None,
            {
                'fields': ('title', 'description', 'project', 'task', 'status', 'priority')
            }
        )
    ]
