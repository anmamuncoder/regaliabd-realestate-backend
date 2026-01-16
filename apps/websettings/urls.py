from django.contrib import admin 
from django.urls import path,include
from .views import WebSettingView


from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register("setting",WebSettingView,basename='web_setting')

urlpatterns = ( 
    [

    ]   + routers.urls
)
