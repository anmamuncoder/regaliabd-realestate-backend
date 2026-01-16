from rest_framework import serializers
from .models import Page, SliderImage


class SliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImage
        fields = "__all__"


class PageSerializer(serializers.ModelSerializer):
    sliders = SliderImageSerializer(
        source="sliderimage_set",  # reverse relation
        many=True,
        read_only=True
    )

    class Meta:
        model = Page
        fields = "__all__"
