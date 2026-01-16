from django.contrib import admin
from .models import Page, SliderImage

 

# ------------------ Page Admin ------------------
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('page', 'title', 'tag')
    search_fields = ('title', 'description', 'tag')
    ordering = ('page',) 

# ------------------ SliderImage Admin ------------------
@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('heading', 'page', 'order', 'button_one_name', 'button_two_name')
    list_filter = ('page',)
    search_fields = ('heading', 'description', 'tag', 'button_one_name', 'button_two_name')
    ordering = ('order',)
    readonly_fields = ('image_preview',)

    fieldsets = (
        (None, {
            'fields': ('page', 'image', 'image_preview', 'heading', 'description', 'tag')
        }),
        ('Buttons', {
            'fields': (
                ('button_one_name', 'button_one_link'),
                ('button_two_name', 'button_two_link')
            )
        }),
        ('Settings', {
            'fields': ('order',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 150px; height:auto;" />'
        return "-"
    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'
