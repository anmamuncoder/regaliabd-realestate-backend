from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here. 
from .models import Project
from .serializers import  ProjectSerializer

class ProjectView(ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
