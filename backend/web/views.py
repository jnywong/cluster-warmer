from django.views.generic import TemplateView
from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from .models import Cluster, Event
from .serializers import ClusterSerializer, EventSerializer
from .tasks import increase_nodepool


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
        response = self.create(request)
        event_id = response.data["id"]
        event = Event.objects.get(id=event_id)
        start_time = event.start_time
        num = event.num_users
        machine = event.machine
        result = increase_nodepool.apply_async(args=[num, machine], eta=start_time)
        # result = increase_nodepool.apply_async(args=[num, machine], countdown=15)
        event.task_submitted = True
        event.task_id = result.id
        return response
