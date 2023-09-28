from django.urls import include, path

urlpatterns = [
    path("revenue/", include("revenue.urls")),
    path("spend/", include("spend.urls")),
]
