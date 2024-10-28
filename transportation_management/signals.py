from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Vehicle, AssignmentLog

@receiver(post_save, sender=Vehicle)
def create_assignment_log(sender, instance, created, **kwargs):
    """
    Signal triggered after saving a Vehicle instance.
    Creates a log entry in AssignmentLog whenever a vehicle is assigned to a route.
    """
    # Check if the vehicle has been assigned to a route
    if instance.route_id is not None:
        # Create a new AssignmentLog entry
        AssignmentLog.objects.create(
            vehicle_license_plate=instance.license_plate,
            route_name=instance.route_id.name,
            assignment_date=timezone.now()
        )
