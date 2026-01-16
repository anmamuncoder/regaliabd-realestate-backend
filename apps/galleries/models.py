from django.db import models
from apps.base.models import BaseModel

# -------------------------
# Photo Gallery
# -------------------------
class PhotoGallery(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='gallery/photos/')
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, help_text="lower numbers show first")

    class Meta:
        verbose_name = "Photo Gallery"
        verbose_name_plural = "Photo Galleries"
        ordering = ['-order']

    def __str__(self):
        return self.title or "Photo"

# -------------------------
# Video Gallery
# -------------------------
class VideoGallery(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    video_url = models.URLField(help_text="YouTube or Vimeo link")
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, help_text="lower numbers show first")

    class Meta:
        verbose_name = "Video Gallery"
        verbose_name_plural = "Video Galleries"
        ordering = ['-order']

    def __str__(self):
        return self.title or "Video"

# -------------------------
# Document Gallery
# -------------------------
class DocumentGallery(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    document = models.FileField(upload_to='gallery/documents/')
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, help_text="lower numbers show first")

    class Meta:
        verbose_name = "Document Gallery"
        verbose_name_plural = "Document Galleries"
        ordering = ['-order']

    def __str__(self):
        return self.title or "Document"
