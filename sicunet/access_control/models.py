"""Models for Access Control System"""

from django.db import models

# Create your models here.


class AccessLog(models.Model):
     """Model to log access control events.""" 
     card_id = models.CharField(max_length=100, unique=True)
     door_name = models.CharField(max_length=100)
     access_granted = models.BooleanField(default=False)
     timestamp = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
         return f"Card ID: {self.card_id} | Door: {self.door_name} | Access Granted: {self.access_granted} | Time: {self.timestamp}"
     
    