from django.contrib import admin 
from django.urls import path,include
from .views import ProjectView


from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register("projects",ProjectView,basename='projects')

urlpatterns = ( 
    [

    ]   + routers.urls
)
