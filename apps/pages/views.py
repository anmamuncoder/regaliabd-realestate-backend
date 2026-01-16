from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here. 
from .models import Page
from .serializers import PageSerializer

class PageView(ReadOnlyModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
