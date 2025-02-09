from django.conf import settings
from django.core.management.base import BaseCommand
from google.cloud import container_v1
from web.models import Cluster


class Command(BaseCommand):
    help = "Reads cluster information from GKE and updates database."

    def __init__(self):
        """
        Get [vCPUs, memory (GB)] from machine types.
        """
        self._dict = {
            "e2-medium": [
                1,
                4,
            ],  # e2-medium: 2 vCPUs, 50% of CPU time = 100% CPU time and effectively consuming 1 core.
            "n2-standard-2": [
                2,
                8,
            ],  # https://cloud.google.com/compute/docs/general-purpose-machines#n2_series
        }

    def parse_response(self, input_data):
        for i in range(len(input_data.node_pools)):
            obj = input_data.node_pools[i]
            if obj.name != "core":
                try:
                    c = Cluster.objects.get(name=obj.name)
                    print(
                        f"Nodepool {obj.name} already in database."
                    )  # TODO: add case where nodepool name is the same but the machine type has changed
                except Cluster.DoesNotExist:
                    print(f"Create new database entry: {obj.name}")
                    c = Cluster(
                        name=obj.name,
                        machine_type=obj.config.machine_type,
                        cpus=self._dict[obj.config.machine_type][0],
                        memory=self._dict[obj.config.machine_type][1],
                    )
                    c.save()

    def handle(self, *args, **options):
        # Create a client
        client = container_v1.ClusterManagerClient(credentials=settings.GCP_CREDENTIALS)

        # Initialize request argument(s)
        request = container_v1.ListClustersRequest()
        name = f"projects/{settings.GCP_PROJECT_ID}/locations/{settings.GCP_ZONE}/clusters/{settings.GCP_CLUSTER}"
        request.parent = name

        # Make the request
        response = client.list_clusters(request=request)

        self.parse_response(response.clusters[0])
