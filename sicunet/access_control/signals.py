"""Signals for Access Control System"""


from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from access_control.models import AccessLog
from datetime import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'access_log.txt')

@receiver(post_save, sender=AccessLog)
def log_access_create(sender, instance, created, **kwargs):
    """Log access control events to a file upon creation."""
    if created:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        status = 'GRANTED' if instance.access_granted else 'DENIED'
        message = f"[{timestamp}] CREATE: Access {status} for Card ID: {instance.card_id} at Door: {instance.door_name}\n"
        
        # Pythonic way to append to file
        with open(LOG_FILE, 'a') as f:
            f.write(message)

@receiver(post_delete, sender=AccessLog)
def log_access_delete(sender, instance, **kwargs):
    """Log access control events to a file upon deletion."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"[{timestamp}] DELETE: Access log deleted for Card ID: {instance.card_id} at Door: {instance.door_name}\n"
    
    with open(LOG_FILE, 'a') as f:
        f.write(message)
