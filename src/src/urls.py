"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls
from web.views import homeViews

schema_view = get_schema_view(
    openapi.Info(
        title="CR API",
        default_version='v1',
        description="Test description",
        terms_of_service="",
        contact=openapi.Contact(email="abdoulmalikkondi8@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', view=homeViews.dashboard, name="index"),
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')),
    path('api/', include('api.urls')),
    path('docs/', include_docs_urls(title='Boptel Rental API')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("__reload__/", include("django_browser_reload.urls")),
] 

urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(prefix=settings.STATIC_URL, document_root=settings.STATIC_ROOT)

