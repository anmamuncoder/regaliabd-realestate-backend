from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Contact Info', {
            'fields': ('name', 'email', 'phone', 'subject', 'message')
        }),
        ('Status & Timing', {
            'fields': ('created_at', 'updated_at')
        }),
    )
