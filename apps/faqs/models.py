from django.db import models
from apps.base.models import BaseModel

# -------------------------
# FAQ Category
# -------------------------
class FAQCategory(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "FAQ Category"
        verbose_name_plural = "FAQ Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

# -------------------------
# FAQ
# -------------------------
class FAQ(BaseModel):
    category = models.ForeignKey(
        FAQCategory, 
        on_delete=models.CASCADE, 
        related_name='faqs'
    )
    question = models.CharField(max_length=500)
    answer = models.TextField()
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.question
