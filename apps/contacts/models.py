from django.db import models
from apps.base.models import BaseModel

class Contact(BaseModel):  
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField() 

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at'] 

    def __str__(self):
        return f"{self.name} - {self.subject or 'No Subject'}"
