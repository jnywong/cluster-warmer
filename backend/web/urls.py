from django.urls import include, path
from rest_framework import routers
from web.views import ClusterViewSet, EventViewSet, IndexView

router = routers.DefaultRouter()
router.register(r"cluster", ClusterViewSet)
# router.register(r"events", EventViewSet)

# Custom binding for EventViewSet

event_list = EventViewSet.as_view({"get": "list", "post": "create_and_submit"})

event_detail = EventViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/", include(router.urls)),
    path("api/events/", event_list, name="event-list"),
    path("api/events/<int:pk>/", event_detail, name="event-detail"),
]
