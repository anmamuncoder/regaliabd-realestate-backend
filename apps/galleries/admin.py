from django.contrib import admin
from .models import PhotoGallery, VideoGallery, DocumentGallery

@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'created_at')
    list_filter = ('featured', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', 'featured', 'created_at')
    list_filter = ('featured', 'created_at')
    search_fields = ('title', 'video_url')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(DocumentGallery)
class DocumentGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'document', 'featured', 'created_at')
    list_filter = ('featured', 'created_at')
    search_fields = ('title', 'document')
    readonly_fields = ('created_at', 'updated_at')
