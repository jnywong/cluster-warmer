import logging

from asgiref.sync import async_to_sync
from celery import shared_task
from django.conf import settings
from google.cloud import container_v1
from web.models import Cluster

logger = logging.getLogger(__name__)


def get_name(machine):
    nodepool_name = Cluster.objects.get(machine_type=machine).name
    name = (
        f"projects/{settings.GCP_PROJECT_ID}/locations/{settings.GCP_ZONE}/clusters/"
        f"{settings.GCP_CLUSTER}/nodePools/{nodepool_name}"
    )
    return name


async def increase_min_node_count(name, num):
    client = container_v1.ClusterManagerAsyncClient(
        credentials=settings.GCP_CREDENTIALS
    )
    request = container_v1.GetNodePoolRequest(
        name=name
    )  # Get current autoscaling config
    response_get = await client.get_node_pool(request=request)

    config = container_v1.NodePoolAutoscaling(
        enabled=response_get.autoscaling.enabled,
        min_node_count=response_get.autoscaling.min_node_count + num,
        max_node_count=response_get.autoscaling.max_node_count,
        location_policy=response_get.autoscaling.location_policy,
    )
    request = container_v1.SetNodePoolAutoscalingRequest(name=name, autoscaling=config)
    await client.set_node_pool_autoscaling(request=request)
    return response_get.autoscaling.min_node_count


async def increase_node_pool_size(min_node_count, name, num):
    client = container_v1.ClusterManagerAsyncClient(
        credentials=settings.GCP_CREDENTIALS
    )
    request = container_v1.SetNodePoolSizeRequest(
        name=name, node_count=min_node_count + num
    )
    await client.set_node_pool_size(request=request)


@shared_task
def increase_nodepool(num, machine):
    """
    Celery task to increase MINIMUM node count in nodepool.

    Increase the minimum node count with set_node_pool_autoscaling().

    NOTE: set_node_pool_autoscaling() does not actually bring nodes up, you need to
    also increase the size of the nodepool with set_node_pool_size() to warm the cluster up.
    """
    min_node_count = async_to_sync(increase_min_node_count)(get_name(machine), num)
    return min_node_count


@shared_task
def increase_nodes(min_node_count, num, machine):
    async_to_sync(increase_node_pool_size)(min_node_count, get_name(machine), num)
