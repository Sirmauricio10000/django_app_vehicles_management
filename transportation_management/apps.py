from django.apps import AppConfig


class TransportationManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transportation_management'

    def ready(self):
        import transportation_management.signals 
