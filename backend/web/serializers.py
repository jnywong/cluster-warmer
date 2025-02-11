from django_celery_results.models import TaskResult
from rest_framework import serializers

from .models import Cluster, Event


class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class NodepoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ["date_created", "task_id", "result"]
