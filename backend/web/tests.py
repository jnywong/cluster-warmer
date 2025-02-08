from django.test import TestCase
from rest_framework.test import RequestsClient


class testAPI(TestCase):
    """
    Test the API.
    """

    def get_client(self):
        self.client = RequestsClient()

    def test_api_event(self):
        client = self.client
        response = client.get("http://testserver/api/events/")
        assert response.status_code == 200
