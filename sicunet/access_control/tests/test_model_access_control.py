"""Tests for AccessLog model in Access Control System"""


from django.test import TestCase
from access_control.models import AccessLog



class AccessLogModelTest(TestCase):
     """Test case for AccessLog model."""
     def setUp(self):
          """Set up test data for AccessLog model tests."""
          self.access_log = AccessLog.objects.create(
               card_id="123456",
               door_name="Main Entrance",
               access_granted=True
          )
     
     def test_access_log_creation(self):
          """Test that an AccessLog instance is created correctly."""
          self.assertEqual(self.access_log.card_id, "123456")
          self.assertEqual(self.access_log.door_name, "Main Entrance")
          self.assertTrue(self.access_log.access_granted)
          self.assertIsNotNone(self.access_log.timestamp)
     
     def test_access_log_str_representation(self):
          """Test the string representation of the AccessLog model."""
          expected_str = f"Card ID: {self.access_log.card_id} | Door: {self.access_log.door_name} | Access Granted: {self.access_log.access_granted} | Time: {self.access_log.timestamp}"
          self.assertEqual(str(self.access_log), expected_str)
          
