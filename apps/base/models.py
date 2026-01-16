from django.db import models 
import uuid
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError

# Create your models here.
class BaseModel(models.Model):
    id = models.CharField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)

    class Meta:
        abstract = True
 
 
class LimitedModel(models.Model):
    MAX_OBJECTS = 1  

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        
        if self.MAX_OBJECTS is not None:
            if self.__class__.objects.count() >= self.MAX_OBJECTS:
                raise ValidationError(
                    f"Cannot create more than {self.MAX_OBJECTS} object(s) for {self.__class__.__name__}."
                )
        super().save(*args, **kwargs)
