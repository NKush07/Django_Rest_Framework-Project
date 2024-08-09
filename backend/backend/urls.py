
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="First Backend APIS",
        default_version='1.0.0',
        description="This is Swagger for our APIS"          
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
]
