from rest_framework import serializers
from .models import PhotoGallery, VideoGallery, DocumentGallery


class PhotoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = "__all__"


class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = "__all__"


class DocumentGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentGallery
        fields = "__all__"
