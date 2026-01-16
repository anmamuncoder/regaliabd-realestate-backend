from django.contrib import admin 
from django.urls import path,include
from .views import PageView


from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register("pages",PageView,basename='pages')

urlpatterns = ( 
    [

    ]   + routers.urls
)
