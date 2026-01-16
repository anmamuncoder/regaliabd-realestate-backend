from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here.
from .serializers import PhotoGallerySerializer, VideoGallerySerializer, DocumentGallerySerializer
from .models import PhotoGallery, VideoGallery, DocumentGallery


class PhotoGalleryView(ReadOnlyModelViewSet):
    serializer_class = PhotoGallerySerializer
    queryset = PhotoGallery.objects.all()

class VideoGalleryView(ReadOnlyModelViewSet):
    serializer_class = VideoGallerySerializer
    queryset = VideoGallery.objects.all()

class DocumentGalleryView(ReadOnlyModelViewSet):
    serializer_class = DocumentGallerySerializer
    queryset = DocumentGallery.objects.all()
