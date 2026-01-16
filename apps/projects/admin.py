from django.contrib import admin
from .models import Project, ProjectImage
 
# -------------------------
# Project Admin
# -------------------------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'property_type',
        'status',
        'featured',
        'price',
        'city',
        'created_at',
    )
    list_filter = ('status', 'featured', 'property_type', 'city', 'created_at')
    search_fields = ('title', 'description', 'city', 'state', 'address')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'description', 'property_type', 'status', 'featured')
        }),
        ('Price & Size', {
            'fields': ('price', 'size_sqft', 'bedrooms', 'bathrooms')
        }),
        ('Location', {
            'fields': ('address', 'city', 'state', 'country', 'postal_code', 'latitude', 'longitude')
        }),
        ('Images', {
            'fields': ('main_image',)
        }),
        ('System Info', {
            'fields': ('created_at', 'updated_at')
        }),
    ) 

    prepopulated_fields = {'slug': ('title',)}  # auto-fill slug from title

# -------------------------
# ProjectImage Admin
# -------------------------
@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption', 'image')
    search_fields = ('caption', 'project__title')
