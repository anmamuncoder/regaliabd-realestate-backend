 
from django.contrib import admin 
from django.urls import path,include
from drf_spectacular.views import ( SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView,)
from .views import home_index_page 

drf_spectacular_urls = [ 
    # OpenAPI schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc UI (optional)
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

apps_urls = [
    path('api/',include('apps.websettings.urls')),
    path('api/',include('apps.pages.urls')),
    path('api/',include('apps.galleries.urls')),
    path('api/',include('apps.projects.urls')),
    path('api/',include('apps.faqs.urls')),
    path('api/',include('apps.contacts.urls')),
]

urlpatterns = ( 
    [
        path("admin/", admin.site.urls),
        path("",home_index_page,name='home'),

    ]   
    +   drf_spectacular_urls
    +   apps_urls
)