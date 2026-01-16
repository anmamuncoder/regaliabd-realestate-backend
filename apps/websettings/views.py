from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here.
from .models import WebSetting
from .serializers import WebSettingSerializer

class WebSettingView(ReadOnlyModelViewSet):
    serializer_class = WebSettingSerializer
    queryset = WebSetting.objects.all()
