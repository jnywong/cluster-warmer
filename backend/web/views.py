from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer


class IndexView(TemplateView):
    """
    Index page.
    """

    template_name = "index.html"


class EventViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing event instances.
    """

    serializer_class = EventSerializer
    queryset = Event.objects.all()
