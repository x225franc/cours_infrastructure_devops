"""
Root URL configuration for meteo-api.
"""

from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

def metrics(request):
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # Prometheus metrics (support both /metrics and /metrics/)
    path("metrics", metrics, name="prometheus-metrics"),
    path("metrics/", metrics, name="prometheus-metrics-slash"),
    # API v1
    path("api/v1/", include("weather.urls")),
    # OpenAPI schema and documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
