from django.contrib import admin 
from django.urls import path,include
from .views import PhotoGalleryView,VideoGalleryView,DocumentGalleryView

from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register("photos",PhotoGalleryView,basename='photos')
routers.register("videos",VideoGalleryView,basename='videos')
routers.register("documents",DocumentGalleryView,basename='documents')

urlpatterns = ( 
    [
        path('galeries/',include(routers.urls))
    ]
)
