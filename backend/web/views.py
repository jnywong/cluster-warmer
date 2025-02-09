from django.views.generic import TemplateView
from rest_framework import mixins, viewsets

from .models import Cluster, Event
from .serializers import ClusterSerializer, EventSerializer


class IndexView(TemplateView):
    """
    Index page.
    """

    template_name = "index.html"


class ClusterViewSet(
    viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin
):
    """
    A viewset for cluster information.
    """

    serializer_class = ClusterSerializer
    queryset = Cluster.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing event instances.
    """

    serializer_class = EventSerializer
    queryset = Event.objects.all()
