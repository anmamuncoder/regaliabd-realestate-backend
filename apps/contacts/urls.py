from django.contrib import admin 
from django.urls import path,include
from .views import ContactCreateAPIView
urlpatterns = ( 
    [
        path("contact/", ContactCreateAPIView.as_view(), name="contact-create"),
    ] 
)
