from django.urls import path, include
from rest_framework import routers
from .views import SpendStatisticViewSet

router = routers.DefaultRouter()
router.register("", SpendStatisticViewSet, basename="spend")

urlpatterns = [
    path("analyze/", SpendStatisticViewSet.as_view({"get": "analyze"}), name="revenue-analyze"),
    path("", include(router.urls)),
]
