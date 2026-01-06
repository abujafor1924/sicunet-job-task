

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from access_control.models import AccessLog


class AccessControlViewTests(APITestCase):
    def setUp(self):
        self.access_log = AccessLog.objects.create(
            card_id="123456",
            door_name="Main Entrance",
            access_granted=True
        )

    def test_access_log_creation(self):
        """Test creating an access log entry."""
        url = reverse('access-log-list')
        data = {
            "card_id": "654321",
            "door_name": "Side Entrance",
            "access_granted": False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AccessLog.objects.count(), 2)
        self.assertEqual(AccessLog.objects.get(card_id="654321").door_name, "Side Entrance")

    def test_access_log_retrieval(self):
        """Test retrieving an access log entry."""
        url = reverse('access-log-detail', args=[self.access_log.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['card_id'], self.access_log.card_id)

