from django.contrib import admin
from .models import FAQCategory, FAQ
 
# -------------------------
# FAQCategory Admin
# -------------------------
@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description') 
    readonly_fields = ('created_at', 'updated_at')

# -------------------------
# FAQ Admin
# -------------------------
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'featured', 'order', 'created_at')
    list_filter = ('category', 'featured', 'created_at')
    search_fields = ('question', 'answer', 'category__name')
    readonly_fields = ('created_at', 'updated_at')
