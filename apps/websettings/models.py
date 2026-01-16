from django.db import models
from apps.base.models import BaseModel,LimitedModel
from django.core.exceptions import ValidationError

class WebSetting(BaseModel,LimitedModel):  
    site_name = models.CharField(max_length=200)
    site_title = models.CharField(max_length=200)
    site_logo = models.ImageField(upload_to='site/logo/', blank=True, null=True)

    # Contact Information
    email = models.EmailField()
    phone_primary = models.CharField(max_length=20)
    phone_secondary = models.CharField(max_length=20, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)

    # Location Information
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, default='Bangladesh')
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    # Google Map / Coordinates
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    google_map_embed_url = models.TextField(blank=True, null=True)

    # Social Media Links
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)

    # Extra Info
    office_open_time = models.CharField(max_length=100, blank=True, null=True)
    office_close_time = models.CharField(max_length=100, blank=True, null=True)
    footer_text = models.TextField(blank=True, null=True) 

    MAX_OBJECTS = 1
 
    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"   
        
    def __str__(self):
        return self.site_name
 