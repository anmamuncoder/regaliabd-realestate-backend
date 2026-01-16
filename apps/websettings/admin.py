from django.contrib import admin
from .models import WebSetting


@admin.register(WebSetting)
class WebSettingAdmin(admin.ModelAdmin):
    list_display = (
        'site_name',
        'site_title',
        'email',
        'phone_primary',
        'city',
        'country',
        'created_at',
    )

    search_fields = (
        'site_name',
        'site_title',
        'email',
        'phone_primary',
        'city',
        'country',
    )

    list_filter = ('country', 'city')

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Site Information', {
            'fields': (
                'site_name',
                'site_title',
                'site_logo',
            )
        }),

        ('Contact Information', {
            'fields': (
                'email',
                'phone_primary',
                'phone_secondary',
                'whatsapp_number',
            )
        }),

        ('Location Information', {
            'fields': (
                'address',
                'city',
                'state',
                'country',
                'postal_code',
            )
        }),

        ('Map & Coordinates', {
            'fields': (
                'latitude',
                'longitude',
                'google_map_embed_url',
            )
        }),

        ('Social Media Links', {
            'fields': (
                'facebook_url',
                'twitter_url',
                'linkedin_url',
                'instagram_url',
                'youtube_url',
            )
        }),

        ('Office & Footer', {
            'fields': (
                'office_open_time',
                'office_close_time',
                'footer_text',
            )
        }),

        ('System Info', {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )
    def clean(self):
            cleaned_data = super().clean()

            if not self.instance.pk and WebSetting.objects.exists():
                raise forms.ValidationError(
                    "Only one Website Setting is allowed. Please edit the existing one."
                )

            return cleaned_data