from asgiref.sync import async_to_sync, sync_to_async
from django.conf import settings
from django.views.generic import TemplateView
from google.cloud import container_v1


async def list_clusters():
    # Create an async client
    client = container_v1.ClusterManagerAsyncClient(
        credentials=settings.GCP_CREDENTIALS
    )

    # Initialize request argument(s)
    request = container_v1.ListClustersRequest()
    name = f"projects/{settings.GCP_PROJECT_ID}/locations/{settings.GCP_ZONE}/clusters/{settings.GCP_CLUSTER}"
    request.parent = name

    # Make the async request
    response = await client.list_clusters(request=request)

    return response.clusters[0]


class IndexView(TemplateView):
    template_name = "index.html"

    async def get_context_data(self, **kwargs):
        context = await sync_to_async(super().get_context_data)(**kwargs)
        clusters = await list_clusters()
        context["clusters"] = clusters
        return context

    def get(self, request, *args, **kwargs):
        context = async_to_sync(self.get_context_data)()
        return self.render_to_response(context)
