from django.db import models
from .constants import PAGES
from apps.base.models import BaseModel  # Assuming BaseModel has created_at, updated_at, etc.

class Page(BaseModel):
    page = models.CharField(max_length=20, choices=PAGES, unique=True)
    title = models.CharField(max_length=150, help_text="Write here a title of the page!")
    description = models.TextField(help_text="Write here description of the page!")
    tag = models.CharField(max_length=50, help_text="Write here a short tag of the page!", blank=True)

     
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return f"{self.get_page_display()}"

  

class SliderImage(BaseModel):
    page = models.ForeignKey(Page,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='slider/', help_text="Upload slider image")
    heading = models.CharField(max_length=150, help_text="Write here a heading for the slider!")
    description = models.TextField(help_text="Write here description for the slider!")
    tag = models.CharField(max_length=50, help_text="Write here a short tag for the slider!", blank=True)

    # Button 1
    button_one_name = models.CharField(max_length=50, help_text="Write first button name", blank=True, null=True)
    button_one_link = models.URLField(help_text="Write first button link", blank=True, null=True)

    # Button 2
    button_two_name = models.CharField(max_length=50, help_text="Write second button name", blank=True, null=True)
    button_two_link = models.URLField(help_text="Write second button link", blank=True, null=True)

    order = models.PositiveIntegerField(default=0, help_text="Slider order, lower numbers show first")

    class Meta:
        verbose_name = "Slider Image"
        verbose_name_plural = "Slider Images"
        ordering = ['order'] 

    def __str__(self):
        return f"{self.page} - {self.heading}"
