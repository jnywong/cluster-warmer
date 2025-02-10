import logging

from celery import shared_task
from django.conf import settings
from google.cloud import container_v1
from web.models import Cluster

logger = logging.getLogger(__name__)


@shared_task
def increase_nodepool(num, machine):
    """
    Celery task to increase minimum node count in nodepool.

    Increase the minimum node count with set_node_pool_autoscaling().

    NOTE: set_node_pool_autoscaling() does not actually bring nodes up, you need to
    also increase the size of the nodepool with set_node_pool_size() to warm the cluster up.
    """
    nodepool_name = Cluster.objects.get(machine_type=machine).name
    client = container_v1.ClusterManagerClient(credentials=settings.GCP_CREDENTIALS)
    name = (
        f"projects/{settings.GCP_PROJECT_ID}/locations/{settings.GCP_ZONE}/clusters/"
        f"{settings.GCP_CLUSTER}/nodePools/{nodepool_name}"
    )

    # Get current autoscaling config
    request = container_v1.GetNodePoolRequest()
    request.name = name
    response_get = client.get_node_pool(request=request)

    # Initialise request argument(s)
    config = container_v1.NodePoolAutoscaling(
        enabled=response_get.autoscaling.enabled,
        min_node_count=num,
        max_node_count=response_get.autoscaling.max_node_count,
        location_policy=response_get.autoscaling.location_policy,
    )
    request = container_v1.SetNodePoolAutoscalingRequest(name=name, autoscaling=config)

    # Make the request
    response = client.set_node_pool_autoscaling(request=request)

    return response
