from django.urls import include, path
from rest_framework import routers

from .views import ClusterViewSet, EventViewSet, IndexView

router = routers.DefaultRouter()
router.register(r"cluster", ClusterViewSet)
router.register(r"events", EventViewSet)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/", include(router.urls)),
]
