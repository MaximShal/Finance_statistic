from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from .api_urls import urlpatterns


SchemaView = get_schema_view(
    openapi.Info(
        title="Finance statistic",
        default_version="v1",
        description="Here you can keep statistics of revenue and spend and analyze the results.",
    ),
    public=True,
    patterns=[path("api/v1/", include(urlpatterns))],
)
