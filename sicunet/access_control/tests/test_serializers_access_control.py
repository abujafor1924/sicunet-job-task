"""Tests for AccessLog serializer in Access Control app."""

from django.test import TestCase
from access_control.models import AccessLog

class AccessLogSerializerTest(TestCase):
     """Test case for AccessLog serializer."""
     def setUp(self):
          """Set up test data for AccessLog serializer tests."""
          self.access_log = AccessLog.objects.create(
               card_id="654321",
               door_name="Back Entrance",
               access_granted=False
          )
     
     def test_access_log_serializer_fields(self):
          """Test that AccessLog serializer fields are correct."""
          self.assertEqual(self.access_log.card_id, "654321")
          self.assertEqual(self.access_log.door_name, "Back Entrance")
          self.assertFalse(self.access_log.access_granted)
          self.assertIsNotNone(self.access_log.timestamp)