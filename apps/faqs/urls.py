from django.contrib import admin 
from django.urls import path,include
from .views import FAQCategoryView


from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register("faqs",FAQCategoryView,basename='faqs')

urlpatterns = ( 
    [

    ]   + routers.urls
)
