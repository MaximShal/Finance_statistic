from django.urls import path, include
from rest_framework import routers
from .views import RevenueStatisticViewSet

router = routers.DefaultRouter()
router.register("", RevenueStatisticViewSet, basename="revenue")

urlpatterns = [
    path("analyze/", RevenueStatisticViewSet.as_view({"get": "analyze"}), name="revenue-analyze"),
    path("", include(router.urls)),
]
