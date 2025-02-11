import time

from django.views.generic import TemplateView
from django_celery_results.models import TaskResult
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cluster, Event
from .serializers import ClusterSerializer, EventSerializer, NodepoolSerializer
from .tasks import decrease_nodepool, increase_nodepool, increase_nodes


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
        """
        Create event object and apply celery tasks on POST.
        """
        response = self.create(request)
        event_id = response.data["id"]
        event = Event.objects.get(id=event_id)
        start_time = event.start_time
        end_time = event.end_time
        num = event.num_users
        machine = event.machine
        min_node_count = increase_nodepool.apply_async(
            args=[num, machine], eta=start_time
        ).get()
        # min_node_count = increase_nodepool.apply_async(  # testing
        #     args=[num, machine], countdown=5
        # ).get()
        time.sleep(5)  # Avoid error 400 Cluster is running incompatible operation
        res_inc = increase_nodes.apply_async(args=[min_node_count, num, machine])
        event.task_submitted = True
        event.task_id = res_inc.id
        event.save()
        min_node_count = decrease_nodepool.apply_async(
            args=[num, machine], eta=end_time
        ).get()
        # min_node_count = decrease_nodepool.apply_async(  # testing
        #     args=[num, machine], countdown=60
        # ).get()
        return response


class NodepoolView(APIView):
    """
    View to monitor minimum node counts.
    """

    def get(self, request):
        task_results = TaskResult.objects.filter(task_name="web.tasks.nodepool_size")
        serializer = NodepoolSerializer(task_results, many=True)
        return Response(serializer.data)
