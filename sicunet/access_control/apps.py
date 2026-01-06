from django.apps import AppConfig


class AccessControlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'access_control'
    
    def ready(self):
        """Import signals to connect them."""
        import access_control.signals  # noqa
