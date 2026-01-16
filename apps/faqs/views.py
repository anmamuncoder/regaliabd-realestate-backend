from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here. 
from .models import FAQ,FAQCategory
from .serializers import FAQCategorySerializer

class FAQCategoryView(ReadOnlyModelViewSet):
    serializer_class = FAQCategorySerializer
    queryset = FAQCategory.objects.all()
