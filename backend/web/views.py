from django.views.generic import TemplateView
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=False, methods="POST")
    def create_and_submit(self, request):
        self.create(request)

        return Response("Event created and task submitted.")
